"""Create managedojects_schemas table

Revision ID: e83c5549560c
Revises: 0b7905a9ba5b
Create Date: 2018-02-03 23:20:13.704000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'e83c5549560c'
down_revision = '0b7905a9ba5b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'managedobjects_schemas',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )
    op.execute('ALTER SEQUENCE  managedobjects_schemas_pk_seq RENAME TO seq_managedobjects_schemas_pk')

    managedobjects_schemas = sa.sql.table(
        'managedobjects_schemas',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_managedobjects_schemas_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )

    op.bulk_insert(managedobjects_schemas, [
        {'name': 'ericsson_cm_2g', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'ericsson_cm_3g', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'ericsson_cm_4g', 'parent_pk': 0, 'vendor_pk': 1, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'huawei_cm_2g', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'huawei_cm_3g', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'huawei_cm_4g', 'parent_pk': 0, 'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'zte_cm_2g', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'zte_cm_3g', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'zte_cm_4g', 'parent_pk': 0, 'vendor_pk': 3, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'nokia_cm_2g', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'nokia_cm_3g', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'nokia_cm_4g', 'parent_pk': 0, 'vendor_pk': 4, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'samsung_cm_2g', 'parent_pk': 0, 'vendor_pk': 5, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'samsung_cm_3g', 'parent_pk': 0, 'vendor_pk': 5, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'samsung_cm_4g', 'parent_pk': 0, 'vendor_pk': 5, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        {'name': 'alcatel_cm_2g', 'parent_pk': 0, 'vendor_pk': 6, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'name': 'alcatel_cm_3g', 'parent_pk': 0, 'vendor_pk': 6, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'name': 'alcatel_cm_4g', 'parent_pk': 0, 'vendor_pk': 6, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
    ])

    # Create cm loads table
    op.create_table(
        'cm_loads',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('load_status', sa.CHAR(length=250)), # RUNNING,FAILED,SUCCEEDED
        sa.Column('is_current_load', sa.Boolean, default=False), #
        sa.Column('load_start', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('load_end', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )
    op.execute('ALTER SEQUENCE  cm_loads_pk_seq RENAME TO seq_cm_loads_pk')

def downgrade():
    op.drop_table('managedobjects_schemas')
    op.drop_table('cm_loads')
