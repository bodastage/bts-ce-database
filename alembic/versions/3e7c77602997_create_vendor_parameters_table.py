"""create vendor parameters table

Revision ID: 3e7c77602997
Revises: b45698c3839b
Create Date: 2018-02-03 03:22:50.224000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '3e7c77602997'
down_revision = 'b45698c3839b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'vendor_parameters',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(250), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
        sa.Column('parent_pk', sa.Integer),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
    )
    op.execute('ALTER SEQUENCE  vendor_parameters_pk_seq RENAME TO seq_vendor_parameters_pk')


def downgrade():
    op.drop_table('vendor_parameters')
