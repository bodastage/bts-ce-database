"""create live network gsm cells data

Revision ID: 920b08e9f6ec
Revises: f4334a4861fe
Create Date: 2018-02-05 13:38:24.833000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '920b08e9f6ec'
down_revision = 'f4334a4861fe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'gsm_cells_data',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('cell_pk', sa.Integer, nullable=False),
        sa.Column('ci', sa.Integer, nullable=False),
        sa.Column('bcc', sa.Integer,),
        sa.Column('ncc', sa.Integer,),
        sa.Column('bsic', sa.Integer,),
        sa.Column('bcch', sa.Integer,),
        sa.Column('lac', sa.Integer,),
        sa.Column('latitude', sa.Float,),
        sa.Column('longitude', sa.Float,),
        sa.Column('cgi', sa.String(200),),
        sa.Column('azimuth', sa.Integer,),
        sa.Column('height', sa.Integer,),
        sa.Column('mechanical_tilt', sa.Integer,),
        sa.Column('electrical_tilt', sa.Integer,),
        sa.Column('hsn', sa.Integer, ),
        sa.Column('hopping_type', sa.String(100), ),
        sa.Column('tch_carriers', sa.String(255), ),
        sa.Column('mcc', sa.Integer),
        sa.Column('mnc', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.gsm_cells_data_pk_seq RENAME TO seq_gsm_cells_data_pk')

    op.create_unique_constraint("uq_live_gsm_cells_data", "sites", ["pk", "cell_pk"],"live_network")

def downgrade():
    op.drop_table('gsm_cells_data', schema=u'live_network')

    op.drop_constraint('uq_live_gsm_cells_data', "gsm_cells_data", type='unique', schema='live_network')
