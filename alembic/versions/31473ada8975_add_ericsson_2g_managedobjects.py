"""Add Ericsson 2G managedobjects

Revision ID: 31473ada8975
Revises: 8ad1b210c464
Create Date: 2018-02-13 01:28:02.459000

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = '31473ada8975'
down_revision = '8ad1b210c464'
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
        {'name': 'BSC', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'CHANNEL_GROUP', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'EXTERNAL_CELL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'INNER_CELL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'INTERNAL_CELL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'MSC', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'NREL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'OUTER_CELL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'OVERLAID_CELL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'PRIORITY_PROFILE', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'SITE', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'TG', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'UTRAN_EXTERNAL_CELL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'UTRAN_NREL', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
    ])

def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(1, 1))
