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
        lte_cells_data.name,
        lte_cells_data.cell_pk,
        lte_cells_data.pci,
        lte_cells_data.uarfcn_dl,
        lte_cells_data.uarfcn_ul,
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
       FROM live_network.lte_cells_data
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_lte_cells_data""")
