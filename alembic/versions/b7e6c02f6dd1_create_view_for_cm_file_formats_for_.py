"""create view for cm file formats for supported vendors

Revision ID: b7e6c02f6dd1
Revises: 9ac4b2aee1ce
Create Date: 2018-03-06 02:32:50.914000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7e6c02f6dd1'
down_revision = '9ac4b2aee1ce'
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

