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
     SELECT 
        t1.cell_pk as pk,
        t4."name" as node_name,
        t3."name" as site_name,
        t1.name as cell_name,
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
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_gsm_cells_data""")
