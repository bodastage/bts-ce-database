"""create live network umts cells data table

Revision ID: 1faf6c2610bb
Revises: 1e413e32b9c5
Create Date: 2018-02-05 13:55:34.209000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1faf6c2610bb'
down_revision = '1e413e32b9c5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'umts_cells_data',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('cell_pk', sa.Integer, nullable=False),
        sa.Column('site_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer, nullable=False),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('bch_power', sa.Integer,),
        sa.Column('cell_id', sa.Integer,),
        sa.Column('lac', sa.Integer,),
        sa.Column('latitude', sa.Float, ),
        sa.Column('longitude', sa.Float, ),
        sa.Column('bcch', sa.Integer,),
        sa.Column('lac', sa.Integer,),
        sa.Column('maximum_transmission_power', sa.Integer,),
        sa.Column('secondary_sch_power', sa.Integer, ),
        sa.Column('azimuth', sa.Integer,),
        sa.Column('height', sa.Integer,),
        sa.Column('primary_sch_power', sa.Integer,),
        sa.Column('rac', sa.Integer,),
        sa.Column('sac', sa.Integer,),
        sa.Column('uarfcn_dl', sa.Integer, ),
        sa.Column('uarfcn_ul', sa.Integer, ),
        sa.Column('ura_list', sa.String(255), ),
        sa.Column('cpich_power', sa.Integer, ),
        sa.Column('scrambling_code', sa.Integer, ),
        sa.Column('cell_range', sa.Integer, ),
        sa.Column('site_sector_carrier', sa.String(300), ),
        sa.Column('mcc', sa.Integer, ),
        sa.Column('mnc', sa.Integer, ),
        sa.Column('ura', sa.Text, ),
        sa.Column('pccpch_power', sa.Integer, ),
        sa.Column('sccpch_power', sa.Integer, ),
        sa.Column('sch_power', sa.Integer, ),
        sa.Column('hspda_enabled', sa.Boolean, ),
        sa.Column('hspda_power', sa.Integer, ),
        sa.Column('eagch_power', sa.Integer, ),
        sa.Column('ergch_power', sa.Integer, ),
        sa.Column('ehich_power', sa.Integer, ),
        sa.Column('hsscch_power', sa.Integer, ),
        sa.Column('aich_power', sa.Integer, ),
        sa.Column('pich_power', sa.Integer, ),
        sa.Column('hspda_enabled', sa.Boolean, ),
        sa.Column('max_hsupa_codes', sa.Integer, ),
        sa.Column('localcellid', sa.Integer, ),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.umts_cells_data_pk_seq RENAME TO seq_umts_cells_data_pk')


def downgrade():
    op.drop_table('umts_cells_data', schema=u'live_network')
