"""create live network gsm external cells table

Revision ID: 0e0ceb9a3832
Revises: 24e5cd9f23c2
Create Date: 2018-02-05 14:31:35.335000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e0ceb9a3832'
down_revision = '24e5cd9f23c2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'gsm_external_cells',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('cell_pk', sa.Integer),
        sa.Column('node_pk', sa.Integer,),
        sa.Column('mcc', sa.Integer,),
        sa.Column('mnc', sa.Integer,),
        sa.Column('lac', sa.Integer,),
        sa.Column('bcch', sa.String(200),),
        sa.Column('ncc', sa.Integer,),
        sa.Column('bcc', sa.Integer,),
        sa.Column('ci', sa.Integer,),
        sa.Column('rac', sa.Integer, ),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.gsm_external_cells_pk_seq RENAME TO seq_gsm_external_cells_pk')


def downgrade():
    op.drop_table('gsm_external_cells', schema=u'live_network')
