"""Create table for 4G external cells

Revision ID: 5b8d91271e45
Revises: 0588ebb5527a
Create Date: 2018-05-23 07:29:17.642000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b8d91271e45'
down_revision = '0588ebb5527a'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'lte_external_cells',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('cell_pk', sa.Integer, nullable=False),
        sa.Column('node_pk', sa.Integer,),
        sa.Column('dl_earfcn', sa.Integer,),
        sa.Column('mnc', sa.Integer,),
        sa.Column('mcc', sa.Integer, ),
        sa.Column('localCellId', sa.Integer,),
        sa.Column('pci', sa.Integer, ),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.lte_external_cells_pk_seq RENAME TO seq_lte_external_cells_pk')


def downgrade():
    op.drop_table('lte_external_cells', schema=u'live_network')
