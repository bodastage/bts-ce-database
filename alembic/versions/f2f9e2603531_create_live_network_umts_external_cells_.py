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


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW live_network.vw_umts_external_cells AS
     SELECT umts_external_cells.pk,
        umts_external_cells.name,
        umts_external_cells.cell_pk,
        umts_external_cells.node_pk,
        umts_external_cells.rac,
        umts_external_cells.lac,
        umts_external_cells.primary_cpich_power,
        umts_external_cells.secondary_cpich_power,
        umts_external_cells.uarfcn_dl,
        umts_external_cells.uarfcn_ul,
        umts_external_cells.mnc,
        umts_external_cells.mcc,
        umts_external_cells.rnc_id,
        umts_external_cells.ci
       FROM live_network.umts_external_cells
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_umts_external_cells""")
