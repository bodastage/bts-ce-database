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
        sa.Column('pk', sa.Integer, primary_key=True),
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
        {'name': 'ENBFunction', 'parent_pk': 26, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'EUtranCellFDD', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataAC', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCDMA2000Reselection', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCellMeasGroup', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataControlPlaneTimer', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataCSIRSConfig', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataECellEquipmentFunction', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataEMLP', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataENBFunction', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataENBServicePrior', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataEUtranCellMeasurement', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataEUtranReselection', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataExpConNtf', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataGlobalQoS', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataGlobleSwitchInformation', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataGsmReselection', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataHetNeteICICConfig', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataICIC', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataLoadManagement', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataMobileSpeedHO', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataMobilityManagement', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPciSection', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPDCP', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPhyChannel', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPositionConfig', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPowerControlDL', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPowerControlUL', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPrachFDD', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataQoS', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataQoSDSCPMapping', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataQoSPBRMapping', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataQoSPRIMapping', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataS1Ap', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSecurityManagement', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataServiceDrx', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataServiceMAC', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSIScheduling', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSonCellPolicy', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSonControl', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSoneNBPolicy', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSonPolicyAnr', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSonPolicyX2', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataSPSConfig', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUeEUtranMeasurement', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUeRATMeasurement', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUeTimer', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUtranCellReselectionFDD', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUtranReselectionFDD', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataUtranReselectionTDD', 'parent_pk': 1813, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataX2Ap', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataPubFunctionPara', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'vsDataQoSServiceClass', 'parent_pk': 1812, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
    ])



def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(3, 3))
