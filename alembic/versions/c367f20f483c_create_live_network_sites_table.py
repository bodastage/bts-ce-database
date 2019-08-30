"""create live_network sites table

Revision ID: c367f20f483c
Revises: d66c88e81543
Create Date: 2018-02-05 03:08:50.437000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'c367f20f483c'
down_revision = 'd66c88e81543'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'sites',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('node_pk', sa.Integer),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.sites_pk_seq RENAME TO seq_sites_pk')

    op.create_unique_constraint("uq_site", "sites", ["name", "node_pk", "tech_pk", "vendor_pk"],"live_network")


def downgrade():
    op.drop_constraint('uq_site', "sites", type_='unique', schema='live_network')
    op.drop_table('sites', schema=u'live_network')
