"""create live network UMTS external cells view

Revision ID: f2f9e2603531
Revises: 7ffc4e23252c
Create Date: 2018-02-05 14:53:48.255000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2f9e2603531'
down_revision = '7ffc4e23252c'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext

vw_umts_external_cells = ReplaceableObject(
    'live_network.vw_umts_external_cells',
    """
     SELECT 
        t3.name as NODENAME,
        t1.name AS CELLNAME,
        t1.rac,
        t1.lac,
        t1.uarfcn_dl,
        t1.mnc,
        t1.mcc,
        t1.rnc_id,
        t1.ci,
        t1.psc
       FROM live_network.umts_external_cells t1
       LEFT JOIN live_network.cells t2 ON t1.cell_pk = t2.pk
       LEFT JOIN live_network.nodes t3 on t3.pk = t1.node_pk

    """)

def upgrade():
    op.create_view(vw_umts_external_cells)


def downgrade():
    op.drop_view(vw_umts_external_cells)
