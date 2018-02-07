"""Create vendor cm file formats view

Revision ID: f2c34be045e3
Revises: 32b1c6af83f6
Create Date: 2018-02-07 15:24:46.208000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2c34be045e3'
down_revision = '32b1c6af83f6'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW vw_vendor_cm_file_formats AS
     SELECT 
        t2.name as vendor,
        t3.name as technology,
        t4.label as format
     FROM vendors_cm_file_format_map t1
     INNER JOIN vendors t2 on t2.pk = t1.vendor_pk
     INNER JOIN technologies t3 on t3.pk  = t1.tech_pk
     INNER JOIN cm_file_formats t4 on t4.pk = t1.format_pk
     ORDER BY t2.pk
    """)


def downgrade():
    op.execute("""DROP VIEW vw_vendor_cm_file_formats""")
