"""create live network gsm external cells view

Revision ID: e8ba4a123cfe
Revises: 0e0ceb9a3832
Create Date: 2018-02-05 14:39:01.184000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8ba4a123cfe'
down_revision = '0e0ceb9a3832'
branch_labels = None
depends_on = None


class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext

vw_gsm_external_cells = ReplaceableObject(
    'live_network.vw_gsm_external_cells',
    """
     SELECT 
        t1.name as cellname,
        t3.name as nodename,
        t1.mcc,
        t1.mnc,
        t1.lac,
        t1.bcch,
        t1.ncc,
        t1.bcc,
        t1.ci
       FROM live_network.gsm_external_cells t1
       INNER JOIN live_network.cells t2 ON t1.cell_pk = t2.pk
       LEFT JOIN live_network.nodes t3 on t3.pk = t1.node_pk

    """)

def upgrade():
    op.create_view(vw_gsm_external_cells)


def downgrade():
    op.drop_view(vw_gsm_external_cells)
