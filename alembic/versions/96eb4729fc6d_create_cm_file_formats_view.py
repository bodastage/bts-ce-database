"""Create cm file formats view

Revision ID: 96eb4729fc6d
Revises: fe33bf7f5c52
Create Date: 2018-02-07 14:36:48.642000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96eb4729fc6d'
down_revision = 'fe33bf7f5c52'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW vw_cm_file_formats AS
     SELECT 
        t2.name as vendor,
        t3.name as technology,
        t1.label as format
     FROM cm_file_formats t1
     INNER JOIN vendors t2 on t2.pk = t1.vendor_pk
     INNER JOIN technologies t3 on t3.pk  = t1.tech_pk
     ORDER BY t2.pk
    """)


def downgrade():
    op.execute("""DROP VIEW vw_cm_file_formats""")