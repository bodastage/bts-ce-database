"""Add Nokia 3G managedobjects

Revision ID: e4d6b83d0c0c
Revises: 3d63ace85c4c
Create Date: 2018-02-13 02:05:48.714000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'e4d6b83d0c0c'
down_revision = '3d63ace85c4c'
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
        {'name': 'A2NE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'A2ST', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'A2UT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ACCP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ADJG', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ADJI', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ADJS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ADR4GW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'AMGR', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ANBA', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ANTL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'BFD', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'BFDGRP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'BTSSCW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'CABINET', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'CCFA', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'CERTH', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'CESIF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'CMOB', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'COCO', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'CONNECTOR', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ETHLK', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'FMCG', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'FMCI', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'FMCS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'FTM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'FUUNIT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'HOPG', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'HOPI', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'HOPL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'HOPS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'HW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IAIF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IBFD', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IBFP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IDNS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IDSP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IEIF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IFPG', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IGIF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IHCP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IICP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IMAG', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPBR', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPHB', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPNB', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPNO', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPQM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPRM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPRO', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPSECC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IQOS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ISBFP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ITRKGRP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ITRKOBJ', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IUBSNT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IUCS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IUCSIP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IUO', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IUPS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IUPSIP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IUR', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'IVIF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'L2SWI', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'LCELGW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'LCELW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'MHA', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'MODULE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'MRBTS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'OSPFV2', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'PISCHDLITEM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'PMSCHDLS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'PPTT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'PWNE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'QOS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RMOD', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNAC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNFC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNHSPA', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNMOBI', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNPS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNRLC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RNTRM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'RSTP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SBR4', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SMOD', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SPTT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SRT4', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SRTT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'STPG', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'STPORT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SUBMODULE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SVTT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'SYNC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'TCTT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'TMPAR', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'TOPB', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'TOPF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'TRDE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'TWAMP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'TWAMPR', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'UNI', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'UNIT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'VBTS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'VCCT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'VCEL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'VCTT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'VPCT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'VPTT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'WAC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'WBTS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'WCEL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'WRAB', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
    ])



def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(4, 2))
