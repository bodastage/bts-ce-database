"""create live_network nodes table

Revision ID: d66c88e81543
Revises: 8579697b2bb6
Create Date: 2018-02-05 03:00:57.931000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'd66c88e81543'
down_revision = '8579697b2bb6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'nodes',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.nodes_pk_seq RENAME TO seq_nodes_pk')


def downgrade():
    op.drop_table('nodes',schema=u'live_network')