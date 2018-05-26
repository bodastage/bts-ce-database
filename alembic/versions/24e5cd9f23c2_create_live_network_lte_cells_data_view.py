"""create live network lte cells data view

Revision ID: 24e5cd9f23c2
Revises: cf14532e09cc
Create Date: 2018-02-05 14:25:51.083000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24e5cd9f23c2'
down_revision = 'cf14532e09cc'
branch_labels = None
depends_on = None



class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


vw_lte_cells_data = ReplaceableObject(
    'live_network.vw_lte_cells_data',
    """
    SELECT 
        t3."name" as vendor,
        t5.name AS nodename,
        t4."name" as sitename,
        t1.name AS cellname,
        t1.mcc,
        t1.mnc,
        t1.pci,
        t1.uarfcn_dl,
        t1.uarfcn_ul,
        t1.dl_bandwidth,
        t1.scheduler,
        t1.tac,
        t1.ecgi,
        t1.rach_root_sequence,
        t1.max_tx_power,
        t1.latitude,
        t1.longitude,
        t1.ta_mode,
        t1.ta,
        t1.tx_elements,
        t1.rx_elements,
        t1.azimuth,
        t1.height,
        t1.mechanical_tilt,
        t1.electrical_tilt
       FROM live_network.lte_cells_data t1
       INNER JOIN live_network.cells t2 on t2.pk = t1.cell_pk AND t2.tech_pk = 3
       INNER JOIN live_network.sites t4 on t4.pk = t2.site_pk
       INNER JOIN live_network.nodes t5 on t5.pk = t4.node_pk
       INNER JOIN public.vendors t3 on t3.pk = t2.vendor_pk

    """)


def upgrade():
    op.create_view(vw_lte_cells_data)


def downgrade():
    op.drop_view(vw_lte_cells_data)