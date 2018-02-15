"""Create live network sites view

Revision ID: eab3475f6f35
Revises: 6f5e5720a6da
Create Date: 2018-02-15 14:06:15.365000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eab3475f6f35'
down_revision = '6f5e5720a6da'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW live_network.vw_sites AS
     SELECT t1.pk as id,  t1.name,
        t4.name as node,
        t2.name AS technology,
        t3.name AS vendor,
        t1.date_added
       FROM live_network.sites t1
         LEFT JOIN live_network.nodes t4 ON T4.pk = t1.node_pk
         JOIN technologies t2 ON t2.pk = t1.tech_pk
         JOIN vendors t3 ON t3.pk = t1.vendor_pk
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_sites""")
