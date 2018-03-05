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
    select t1.pk, 
    t4.name as vendor,
    t5.name as technology,
    t3.name as format,
    t3.label as label
    from 
    vendors_cm_file_format_map t1
    INNER JOIN supported_vendor_tech t2 on t2.pk = t1.vendor_tech_pk
    INNER JOIN cm_file_formats t3 on t3.pk = t1.format_pk
    INNER JOIN vendors t4 on t4.pk  = t3.vendor_pk 
    INNER JOIN technologies t5 on t5.pk = t3.tech_pk
    """)


def downgrade():
    op.execute("""DROP VIEW vw_vendor_cm_file_formats""")
