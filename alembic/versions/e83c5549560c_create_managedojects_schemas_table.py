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


def downgrade():
    op.drop_table('managedobjects_schemas')
