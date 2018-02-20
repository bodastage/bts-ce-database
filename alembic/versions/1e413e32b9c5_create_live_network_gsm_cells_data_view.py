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


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW live_network.vw_gsm_cells_data AS
     SELECT gsm_cells_data.pk,
        gsm_cells_data.name,
        gsm_cells_data.cell_pk,
        gsm_cells_data.ci,
        gsm_cells_data.bcc,
        gsm_cells_data.ncc,
        gsm_cells_data.bsic,
        gsm_cells_data.bcch,
        gsm_cells_data.lac,
        gsm_cells_data.latitude,
        gsm_cells_data.longitude,
        gsm_cells_data.cgi,
        gsm_cells_data.azimuth,
        gsm_cells_data.height,
        gsm_cells_data.mechanical_tilt,
        gsm_cells_data.electrical_tilt,
        gsm_cells_data.hsn,
        gsm_cells_data.hopping_type,
        gsm_cells_data.tch_carriers
       FROM live_network.gsm_cells_data
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_gsm_cells_data""")
