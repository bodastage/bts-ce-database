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
        {'name': 'SubNetwork', 'parent_pk': 1721, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1699},
        {'name': 'bulkCmConfigDataFile', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1720},
        {'name': 'configData', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1721},
        {'name': 'fileFooter', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1722},
        {'name': 'fileHeader', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1723},
        {'name': 'GsmCell', 'parent_pk': 1691, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1695},
        {'name': 'ExternalGsmCell', 'parent_pk': 1699, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1693},
        {'name': 'meContext', 'parent_pk': 1700, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1698},
        {'name': 'vsDataAbisLink', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1701},
        {'name': 'vsDataAbisTrPath', 'parent_pk': 1767, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1702},
        {'name': 'vsDataAbisTrPathCir', 'parent_pk': 1702, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1703},
        {'name': 'vsDataALink', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1704},
        {'name': 'vsDataAmrHandoverControl', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1705},
        {'name': 'vsDataBssAmr', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1706},
        {'name': 'vsDataBssDynFreq', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1707},
        {'name': 'vsDataBssEmlpp', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1708},
        {'name': 'vsDataBssFunction', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1709},
        {'name': 'vsDataBssFunctionPS', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1710},
        {'name': 'vsDataBssFunctionRsv', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1711},
        {'name': 'vsDataBssFunctionTimer', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1712},
        {'name': 'vsDataBssFunctionUpRsv', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1713},
        {'name': 'vsDataBssHandoverControl', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1714},
        {'name': 'vsDataBssIfta', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1715},
        {'name': 'vsDataBssPrecisePaging', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1716},
        {'name': 'vsDataBtsEquipment', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1717},
        {'name': 'vsDataBtsLapd', 'parent_pk': 1717, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1718},
        {'name': 'vsDataBtsSiteManager', 'parent_pk': 1691, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1719},
        {'name': 'GsmRelation', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1696},
        {'name': 'BssFunction', 'parent_pk': 1697, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1690},
        {'name': 'ManagedElement', 'parent_pk': 1698, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1697},
        {'name': 'SubNetwork_2', 'parent_pk': 1699, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1700},
        {'name': 'BtsSiteManager', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1691},
        {'name': 'vsDataCellIfta', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1727},
        {'name': 'vsDataCellPrecisePaging', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1728},
        {'name': 'vsDataCellPs', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1729},
        {'name': 'vsDataCellPsNc2', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1730},
        {'name': 'vsDataCellRsv', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1731},
        {'name': 'vsDataCellUpRsv', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1732},
        {'name': 'vsDataCommMeas', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1733},
        {'name': 'vsDataCrrmCellLd', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1734},
        {'name': 'vsDataCrrmNCellLdFDD', 'parent_pk': 1694, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1735},
        {'name': 'vsDataDpi', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1736},
        {'name': 'vsDataDpiAppSrv', 'parent_pk': 1736, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1737},
        {'name': 'vsDataDpiAppSrvPri', 'parent_pk': 1739, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1738},
        {'name': 'vsDataDpiProcMap', 'parent_pk': 1736, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1740},
        {'name': 'vsDataDTM', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1741},
        {'name': 'vsDataDynPwShare', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1742},
        {'name': 'vsDataEhancedEdge', 'parent_pk': 1726, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1743},
        {'name': 'vsDataEutranMeasure', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1745},
        {'name': 'vsDataEutranRelation', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1746},
        {'name': 'vsDataExternalEutranCellFDD', 'parent_pk': 1692, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1747},
        {'name': 'vsDataExternalUtranCellFDD', 'parent_pk': 1694, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1749},
        {'name': 'vsDataFhHandoverControl', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1750},
        {'name': 'vsDataFTPInfoCfg', 'parent_pk': 1752, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1751},
        {'name': 'vsDataFullSignalTrace', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1752},
        {'name': 'vsDataGbLink', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1753},
        {'name': 'vsDataGprsEdgeSchedule', 'parent_pk': 1726, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1754},
        {'name': 'vsDataGsmCell', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1755},
        {'name': 'vsDataGsmVpcRelation', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1757},
        {'name': 'vsDataHandoverControl', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1758},
        {'name': 'vsDataHoppingBaseband', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1759},
        {'name': 'vsDataHoppingFrequency', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1760},
        {'name': 'vsDataIpbm', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1761},
        {'name': 'vsDataIpGbLocalEP', 'parent_pk': 1763, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1762},
        {'name': 'vsDataIpGbNse', 'parent_pk': 1753, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1763},
        {'name': 'vsDataIpSlaExTask', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1764},
        {'name': 'vsDataIurgLink', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1765},
        {'name': 'vsDataLogicalAbisLink', 'parent_pk': 1771, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1767},
        {'name': 'vsDataLogicalALink', 'parent_pk': 1771, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1768},
        {'name': 'vsDataLogicalGbLink', 'parent_pk': 1771, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1769},
        {'name': 'vsDataLogicalIurgLink', 'parent_pk': 1771, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1770},
        {'name': 'vsDataMPlmn', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1771},
        {'name': 'vsDataMscLink', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1772},
        {'name': 'vsDataNACC', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1773},
        {'name': 'vsDataPcuInfo', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1775},
        {'name': 'vsDataPriorityResel', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1777},
        {'name': 'vsDataPsChannelSchedule', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1778},
        {'name': 'vsDataPsHandoverControl', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1779},
        {'name': 'vsDataPsPowerControl', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1780},
        {'name': 'vsDataPsUserAndSrvType', 'parent_pk': 1792, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1781},
        {'name': 'vsDataPwOptimize', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1782},
        {'name': 'vsDataScHandoverControl', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1784},
        {'name': 'vsDataSdHandoverControl', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1785},
        {'name': 'vsDataSignalTraceCfg', 'parent_pk': 1752, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1786},
        {'name': 'vsDataSubCell', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1787},
        {'name': 'vsDataSubCellPsAlloc', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1788},
        {'name': 'vsDataTrx', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1789},
        {'name': 'vsDataTs', 'parent_pk': 1789, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1790},
        {'name': 'vsDataUmsyn', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1791},
        {'name': 'vsDataUserAndSrvBasedSche', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1792},
        {'name': 'vsDataUtranHandoverControl', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1793},
        {'name': 'vsDataUtranMeasure', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1794},
        {'name': 'vsDataVamos', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1796},
        {'name': 'vsDataDpiAppSrvProfile', 'parent_pk': 1736, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1739},
        {'name': 'vsDataExternalGsmCell', 'parent_pk': 1693, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1748},
        {'name': 'vsDataCellEdge', 'parent_pk': 1729, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1726},
        {'name': 'vsDataGsmRelation', 'parent_pk': 1696, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1756},
        {'name': 'vsDataLocationArea', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1766},
        {'name': 'vsDataPowerControl', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1776},
        {'name': 'vsDataRoutingArea', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1783},
        {'name': 'vsDataUtranRelation', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1795},
        {'name': 'vsDataCellAmr', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1725},
        {'name': 'vsDataBvc', 'parent_pk': 1695, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1724},
        {'name': 'vsDataNri', 'parent_pk': 1690, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0,
         'pk': 1774},
        {'name': 'ExternalUtranCellFDD', 'parent_pk': 1694, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1694},
        {'name': 'ExternalEutranCellFDD', 'parent_pk': 1699, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1692},
        {'name': 'vsDataEmlppUserPriority', 'parent_pk': 1708, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0, 'pk': 1744},
    ])

    op.execute("""ALTER SEQUENCE seq_managedobjects_pk RESTART WITH {};""".format(1797))

def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(3, 1))
