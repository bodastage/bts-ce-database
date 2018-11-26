"""create live network lte cells data table

Revision ID: cf14532e09cc
Revises: cfc100311d9f
Create Date: 2018-02-05 14:13:21.604000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf14532e09cc'
down_revision = 'cfc100311d9f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'lte_cells_data',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('cell_pk', sa.Integer, nullable=False),
        sa.Column('dl_uarfcn', sa.Integer,),
        sa.Column('ul_earfcn', sa.Integer,),
        sa.Column('mcc', sa.Integer, ),
        sa.Column('mnc', sa.Integer, ),
        sa.Column('tac', sa.Integer,),
        sa.Column('pci', sa.Integer,),
        sa.Column('ecgi', sa.String(200),),
        sa.Column('rach_root_sequence', sa.String(200),),
        sa.Column('max_tx_power', sa.Integer,),
        sa.Column('latitude', sa.Float,),
        sa.Column('longitude', sa.Float,),
        sa.Column('height', sa.Integer,),
        sa.Column('dl_bandwidth', sa.Integer, ),
        sa.Column('ul_bandwidth', sa.Integer, ),
        sa.Column('ta', sa.Integer,),
        sa.Column('ta_mode', sa.String(100), ),
        sa.Column('tx_elements', sa.Integer, ),
        sa.Column('rx_elements', sa.Integer, ),
        sa.Column('scheduler', sa.Integer, ),
        sa.Column('azimuth', sa.Integer, ),
        sa.Column('mechanical_tilt', sa.Integer, ),
        sa.Column('electrical_tilt', sa.Integer, ),
        sa.Column('cell_range', sa.Integer, ),
        sa.Column('site_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer, nullable=False),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.lte_cells_data_pk_seq RENAME TO seq_lte_cells_data_pk')


def downgrade():
    op.drop_table('lte_cells_data', schema=u'live_network')
