"""Add Nokia 4G managedobjects

Revision ID: bff23d6fb1e7
Revises: e4d6b83d0c0c
Create Date: 2018-02-13 02:07:18.516000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'bff23d6fb1e7'
down_revision = 'e4d6b83d0c0c'
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
        {'name': 'AMGR', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ANRPRL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ANTL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'BFDGRP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'BTSSCL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CERTH', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'CTRLTS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'ETHLK', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'FTM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'GTPU', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'HW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IDNS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IEIF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IHCP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPNO', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPRM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPRT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPRTV6', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IPSECC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'IVIF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'L2SWI', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LCELL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNADJ', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNADJL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNADJW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNBTS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNCEL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNHOW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNMME', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LNREL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'LTAC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'MODULE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'MRBTS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'MTRACE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'OAMPRF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PMCADM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PMRNL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'PMTNL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'QOS', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'REDRT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'RMOD', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SCTP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SMOD', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'STPG', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SUBMODULE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'SYNC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TAC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TOPB', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TOPF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TOPP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'TWAMP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UFFIM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'UNIT', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
    ])


def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(4, 3))
