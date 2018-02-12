"""Add Nokia 2G managedobjects

Revision ID: 3d63ace85c4c
Revises: 5bdfdb4baaa3
Create Date: 2018-02-13 02:03:55.761000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '3d63ace85c4c'
down_revision = '5bdfdb4baaa3'
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
        {'name': 'ADCE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'ADJL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'ADJW', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'BCF', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'DAP', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'GPC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'HOC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'LAPD', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'MAL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'NSVL', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'PCM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'PCU', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'POC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'RA', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'SMLC', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'TCSM', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'TID', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'TRE', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'TRX', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
    ])


def downgrade():
    op.execute("""DELETE FROM managedobjects WHERE vendor_pk = {0} AND tech_pk = {1}""".format(4, 1))
