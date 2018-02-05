"""create base_line_values view

Revision ID: 9b3717bc5552
Revises: 48071f2cf14b
Create Date: 2018-02-05 02:50:53.929000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '9b3717bc5552'
down_revision = '48071f2cf14b'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
     CREATE OR REPLACE VIEW live_network.vw_baseline AS
         SELECT t4.name AS vendor,
         t5.name AS technology,
         t3.nam1e AS mo,
         t2.name AS parameter,
         t1.value,
         t1.date_added,
         t1.date_modified
     FROM live_network.base_line_values t1
     JOIN vendor_parameters t2 ON t2.pk = t1.parameter_pk
     JOIN managedobjects t3 ON t3.pk = t2.parent_pk
     JOIN vendors t4 ON t4.pk = t3.vendor_pk
     JOIN technologies t5 ON t5.pk = t3.tech_pk
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_baseline""")
