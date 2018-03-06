"""Add ZTE 4G managedobjects

Revision ID: 5bdfdb4baaa3
Revises: 287e90f00943
Create Date: 2018-02-13 01:59:28.823000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '5bdfdb4baaa3'
down_revision = '287e90f00943'
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
        {'name': 'bulkCmConfigDataFile', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2020},
        {'name': 'configData', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2021},
        {'name': 'fileFooter', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2022},
        {'name': 'fileHeader', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2023},
        {'name': 'EUtranCellFDD', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 1997},
        {'name': 'EUtranRelation', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 1998},
        {'name': 'ExternalEUtranCellFDD', 'parent_pk': 2006, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 1999},
        {'name': 'ExternalGsmCell', 'parent_pk': 2006, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2000},
        {'name': 'ExternalUtranCellFDD', 'parent_pk': 2006, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2001},
        {'name': 'GsmRelation', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2002},
        {'name': 'ManagedElement', 'parent_pk': 2004, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2003},
        {'name': 'meContext', 'parent_pk': 2006, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2004},
        {'name': 'SubNetwork_2', 'parent_pk': 2005, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2006},
        {'name': 'UtranRelation', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2007},
        {'name': 'vsDataAC', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2008},
        {'name': 'vsDataCellMeasGroup', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2010},
        {'name': 'vsDataControlPlaneTimer', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2011},
        {'name': 'vsDataCSIRSConfig', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2012},
        {'name': 'vsDataECellEquipmentFunction', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2013},
        {'name': 'vsDataEMLP', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2014},
        {'name': 'vsDataENBFunction', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2015},
        {'name': 'vsDataENBServicePrior', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2016},
        {'name': 'vsDataEUtranCellFDD', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2017},
        {'name': 'vsDataEUtranCellMeasurement', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2018},
        {'name': 'vsDataEUtranRelation', 'parent_pk': 1998, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2019},
        {'name': 'vsDataEUtranReselection', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2024},
        {'name': 'vsDataExpConNtf', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2025},
        {'name': 'vsDataExternalEUtranCellFDD', 'parent_pk': 1999, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2026},
        {'name': 'vsDataExternalGsmCell', 'parent_pk': 2000, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2027},
        {'name': 'vsDataGlobalQoS', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2029},
        {'name': 'vsDataGlobleSwitchInformation', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2030},
        {'name': 'vsDataGsmRelation', 'parent_pk': 2002, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2031},
        {'name': 'vsDataGsmReselection', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2032},
        {'name': 'vsDataHetNeteICICConfig', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2033},
        {'name': 'vsDataICIC', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2034},
        {'name': 'vsDataLoadManagement', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2035},
        {'name': 'vsDataManagedElement', 'parent_pk': 2003, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2036},
        {'name': 'vsDataMobileSpeedHO', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2037},
        {'name': 'vsDataMobilityManagement', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2038},
        {'name': 'vsDataPaging', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2039},
        {'name': 'vsDataPciSection', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2040},
        {'name': 'vsDataPDCP', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2041},
        {'name': 'vsDataPhyChannel', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2042},
        {'name': 'vsDataPositionConfig', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2043},
        {'name': 'vsDataPowerControlDL', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2044},
        {'name': 'vsDataPowerControlUL', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2045},
        {'name': 'vsDataPrachFDD', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2046},
        {'name': 'vsDataPubFunctionPara', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2047},
        {'name': 'vsDataQoS', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2048},
        {'name': 'vsDataQoSDSCPMapping', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2049},
        {'name': 'vsDataQoSPBRMapping', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2050},
        {'name': 'vsDataQoSPRIMapping', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2051},
        {'name': 'vsDataQoSServiceClass', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2052},
        {'name': 'vsDataS1Ap', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2053},
        {'name': 'vsDataSecurityManagement', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2054},
        {'name': 'ENBFunction', 'parent_pk': 2003, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 1996},
        {'name': 'vsDataSonCellPolicy', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2058},
        {'name': 'vsDataSonControl', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2059},
        {'name': 'vsDataSoneNBPolicy', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2060},
        {'name': 'vsDataSonPolicyAnr', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2061},
        {'name': 'vsDataSonPolicyX2', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2062},
        {'name': 'vsDataSPSConfig', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2063},
        {'name': 'vsDataUeEUtranMeasurement', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2064},
        {'name': 'vsDataUeRATMeasurement', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2065},
        {'name': 'vsDataUeTimer', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2066},
        {'name': 'vsDataUtranCellReselectionFDD', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2067},
        {'name': 'vsDataUtranRelation', 'parent_pk': 2007, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2068},
        {'name': 'vsDataUtranReselectionFDD', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2069},
        {'name': 'vsDataUtranReselectionTDD', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2070},
        {'name': 'vsDataX2Ap', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2071},
        {'name': 'vsDataServiceMAC', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2056},
        {'name': 'SubNetwork', 'parent_pk': 2021, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2005},
        {'name': 'vsDataCDMA2000Reselection', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2009},
        {'name': 'vsDataSIScheduling', 'parent_pk': 1997, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2057},
        {'name': 'vsDataExternalUtranCellFDD', 'parent_pk': 2001, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2028},
        {'name': 'vsDataServiceDrx', 'parent_pk': 1996, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0, 'pk': 2055},
    ])

    op.execute("""ALTER SEQUENCE seq_managedobjects_pk RESTART WITH {};""".format(2072))



def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(3, 3))
