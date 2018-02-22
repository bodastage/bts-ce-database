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


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW live_network.vw_lte_cells_data AS
     SELECT lte_cells_data.pk,
        lte_cells_data.cell_pk,
        t4."name" as site_name,
        lte_cells_data.name,
        t3."name" as vendor,
        lte_cells_data.mcc,
        lte_cells_data.mnc,
        lte_cells_data.pci,
        lte_cells_data.uarfcn_dl,
        lte_cells_data.uarfcn_ul,
        lte_cells_data.dl_bandwidth,
        lte_cells_data.scheduler,
        lte_cells_data.tac,
        lte_cells_data.ecgi,
        lte_cells_data.rach_root_sequence,
        lte_cells_data.max_tx_power,
        lte_cells_data.latitude,
        lte_cells_data.longitude,
        lte_cells_data.ta_mode,
        lte_cells_data.ta,
        lte_cells_data.tx_elements,
        lte_cells_data.rx_elements,
        lte_cells_data.azimuth,
        lte_cells_data.height,
        lte_cells_data.mechanical_tilt,
        lte_cells_data.electrical_tilt
       FROM live_network.lte_cells_data lte_cells_data
       INNER JOIN live_network.cells t2 on t2.pk = lte_cells_data.cell_pk AND t2.tech_pk = 3
       INNER JOIN live_network.sites t4 on t4.pk = t2.site_pk
       INNER JOIN public.vendors t3 on t3.pk = t2.vendor_pk
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_lte_cells_data""")
