"""create live network UMTS external cells table

Revision ID: 7ffc4e23252c
Revises: e8ba4a123cfe
Create Date: 2018-02-05 14:45:42.961000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ffc4e23252c'
down_revision = 'e8ba4a123cfe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'umts_external_cells',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('cell_pk', sa.Integer),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('node_pk', sa.Integer),
        sa.Column('rac', sa.Integer),
        sa.Column('lac', sa.Integer),
        sa.Column('primary_cpich_power', sa.Float),
        sa.Column('secondary_cpich_power', sa.Float),
        sa.Column('uarfcn_dl', sa.Integer),
        sa.Column('uarfcn_ul', sa.Integer),
        sa.Column('mnc', sa.Integer),
        sa.Column('mcc', sa.Integer),
        sa.Column('rnc_id', sa.Integer),
        sa.Column('ci', sa.Integer),
        sa.Column('rncid', sa.Integer),
        sa.Column('psc', sa.Integer),
        sa.Column('sac', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.umts_external_cells_pk_seq RENAME TO seq_umts_external_cells_pk')


def downgrade():
    op.drop_table('umts_external_cells', schema=u'live_network')
