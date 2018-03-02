"""create vendors table

Revision ID: b45698c3839b
Revises: 
Create Date: 2018-02-03 03:04:14.816000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'b45698c3839b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'vendors',
        sa.Column('pk', sa.Integer, primary_key=True,  nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )
    op.execute('ALTER SEQUENCE  vendors_pk_seq RENAME TO seq_vendors_pk')

    vendors = sa.sql.table(
        'vendors',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_vendors_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(50), unique=True, nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )

    op.bulk_insert(vendors, [
        {'name': 'Ericsson', notes: 'Ericsson AB', 'modified_by': 0, 'added_by': 0},
        {'name': 'Huawei', notes: 'Huawei Technologies Co., Ltd.', 'modified_by': 0, 'added_by': 0},
        {'name': 'ZTE', notes: 'ZTE Corporation', 'modified_by': 0, 'added_by': 0},
        {'name': 'Nokia', notes: 'Nokia Networks', 'modified_by': 0, 'added_by': 0},
        {'name': 'Bodastage', notes: 'Bodastage Solutions', 'modified_by': 0, 'added_by': 0},
        {'name': 'Samsung',  notes: 'Samsung Electronics', 'modified_by': 0, 'added_by': 0},
        {'name': 'Alcatel', notes: 'Alcatel-Lucent S.A.', 'modified_by': 0, 'added_by': 0},
        {'name': 'Siemens', notes: 'Siemens AG', 'modified_by': 0, 'added_by': 0},
        {'name': 'Motorola', notes: 'Motorola, Inc.', 'modified_by': 0, 'added_by': 0},
    ])


def downgrade():
    op.drop_table('vendors')
