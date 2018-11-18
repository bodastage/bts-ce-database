"""
Create live network lte external cells

Revision ID: a5ff5b06e303
Revises: 5b8d91271e45
Create Date: 2018-05-25 13:31:34.051000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5ff5b06e303'
down_revision = '5b8d91271e45'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


vw_lte_external_cells = ReplaceableObject(
    'live_network.vw_lte_external_cells',
    """
     SELECT t4.name AS nodename,
       t3.name AS sitename,
        t1.name AS cellname,
        t1.mnc,
        t1.mcc,
        t1.dl_earfcn,
        t1.pci,
        t1.tac
       FROM live_network.lte_external_cells t1
         LEFT JOIN live_network.cells t2 ON t1.cell_pk = t2.pk
         LEFT JOIN live_network.sites t3 ON t3.pk = t2.site_pk
      LEFT JOIN live_network.nodes t4 ON t4.pk = t1.node_pk
    """)

def upgrade():
    op.create_view(vw_lte_external_cells)


def downgrade():
    op.drop_view(vw_lte_external_cells)