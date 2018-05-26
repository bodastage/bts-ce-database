"""create live network gsm cells data view

Revision ID: 1e413e32b9c5
Revises: 920b08e9f6ec
Create Date: 2018-02-05 13:48:50.560000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e413e32b9c5'
down_revision = '920b08e9f6ec'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


vw_gsm_cells_data = ReplaceableObject(
    'live_network.vw_gsm_cells_data',
    """
      SELECT 
        t5."name" as vendor,
        t4."name" as nodename,
        t3."name" as sitename,
        t1.name as cellname,
        t1.ci,
        t1.bcc,
        t1.ncc,
        t1.bsic,
        t1.bcch,
        t1.lac,
        t1.latitude,
        t1.longitude,
        t1.cgi,
        t1.azimuth,
        t1.height,
        t1.mechanical_tilt,
        t1.electrical_tilt,
        t1.hsn,
        t1.hopping_type,
        t1.tch_carriers
       FROM live_network.gsm_cells_data t1
       INNER JOIN live_network.cells t2 on t1.cell_pk = t2.pk
       INNER JOIN live_network.sites t3 ON t2.site_pk = t3.pk
       INNER JOIN live_network.nodes t4 on t4.pk = t3.node_pk
       JOIN vendors t5 ON t5.pk = t2.vendor_pk
    """)

def upgrade():
    op.create_view(vw_gsm_cells_data)


def downgrade():
    op.drop_view(vw_gsm_cells_data)
