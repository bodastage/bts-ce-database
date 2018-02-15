"""Create live network nodes view

Revision ID: 6f5e5720a6da
Revises: f13003109a9e
Create Date: 2018-02-15 13:10:20.475000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f5e5720a6da'
down_revision = 'f13003109a9e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW live_network.vw_nodes AS
        SELECT t1.pk AS id,
        t1.name AS nodename,
        t1.type,
        t2.name AS technology,
        t3.name AS vendor,
        t1.date_added
        FROM live_network.nodes t1
            JOIN technologies t2 ON t2.pk = t1.tech_pk
            JOIN vendors t3 ON t3.pk = t1.vendor_pk
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_nodes""")
