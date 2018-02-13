"""Add ZTE 2G managedobjects

Revision ID: 667f21d587d3
Revises: 6a16d2aa6b6a
Create Date: 2018-02-13 01:45:43.414000

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = '667f21d587d3'
down_revision = '6a16d2aa6b6a'
branch_labels = None
depends_on = None


def upgrade():

    managedobjects = sa.sql.table(
        'managedobjects',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_managedobjects_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('label', sa.String(200)),
        sa.Column('parent_pk', sa.Integer),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )


    op.bulk_insert(managedobjects, [
        {'name': 'BtsSiteManager', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'ExternalUtranCellFDD', 'parent_pk': 32, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'GsmCell', 'parent_pk': 1559, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'meContext', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataExternalEutranCellFDD', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataAbisTrPath', 'parent_pk': 1623, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataALink', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataAmrHandoverControl', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssAmr', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssDynFreq', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssEmlpp', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssFunction', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssFunctionPS', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssFunctionRsv', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssFunctionTimer', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssFunctionUpRsv', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssHandoverControl', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssIfta', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBssPrecisePaging', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBtsEquipment', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBtsLapd', 'parent_pk': 1580, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBtsSiteManager', 'parent_pk': 1559, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataBvc', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellAmr', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellEdge', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellIfta', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellPrecisePaging', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellPs', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellPsNc2', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellRsv', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellUpRsv', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCommMeas', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCrrmCellLd', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataDpi', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataDpiAppSrv', 'parent_pk': 1595, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataDpiAppSrvPri', 'parent_pk': 1598, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataDpiAppSrvProfile', 'parent_pk': 1595, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataDpiProcMap', 'parent_pk': 1595, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataDTM', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataDynPwShare', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataEhancedEdge', 'parent_pk': 1585, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataEmlppUserPriority', 'parent_pk': 1571, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataEutranMeasure', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataEutranRelation', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataExternalUtranCellFDD', 'parent_pk': 1561, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataFhHandoverControl', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataFTPInfoCfg', 'parent_pk': 1610, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataFullSignalTrace', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataGbLink', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataGprsEdgeSchedule', 'parent_pk': 1585, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataGsmCell', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataGsmVpcRelation', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataHandoverControl', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataHoppingBaseband', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataHoppingFrequency', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataIpbm', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataIpGbLocalEP', 'parent_pk': 1620, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataIpGbNse', 'parent_pk': 1611, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataIpSlaExTask', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataIurgLink', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataLogicalAbisLink', 'parent_pk': 1627, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataLogicalALink', 'parent_pk': 1627, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataLogicalGbLink', 'parent_pk': 1627, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataMPlmn', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataMscLink', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataNACC', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataNri', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPcuInfo', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPriorityResel', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPsChannelSchedule', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPsPowerControl', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPsUserAndSrvType', 'parent_pk': 1646, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPwOptimize', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataScHandoverControl', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSdHandoverControl', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSignalTraceCfg', 'parent_pk': 1610, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSubCell', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSubCellPsAlloc', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataTrx', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataTs', 'parent_pk': 1643, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUmsyn', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUserAndSrvBasedSche', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUtranHandoverControl', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUtranMeasure', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataVamos', 'parent_pk': 1562, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'BssFunction', 'parent_pk': 26, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'ExternalEutranCellFDD', 'parent_pk': 32, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataAbisLink', 'parent_pk': 1558, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataAbisTrPathCir', 'parent_pk': 1565, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCrrmNCellLdFDD', 'parent_pk': 1561, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataLogicalIurgLink', 'parent_pk': 1627, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPsHandoverControl', 'parent_pk': 1588, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
    ])


def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(3, 1))
