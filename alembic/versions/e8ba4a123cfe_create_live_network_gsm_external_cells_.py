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


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW live_network.vw_gsm_external_cells AS
     SELECT gsm_external_cells.pk,
        gsm_external_cells.name,
        gsm_external_cells.cell_pk,
        gsm_external_cells.node_pk,
        gsm_external_cells.mcc,
        gsm_external_cells.mnc,
        gsm_external_cells.lac,
        gsm_external_cells.bcch,
        gsm_external_cells.ncc,
        gsm_external_cells.bcc,
        gsm_external_cells.ci
       FROM live_network.gsm_external_cells
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_gsm_external_cells""")
