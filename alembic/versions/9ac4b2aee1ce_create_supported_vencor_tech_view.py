"""Create supported vencor tech view

Revision ID: 9ac4b2aee1ce
Revises: b85d15633234
Create Date: 2018-03-03 03:28:35.991000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ac4b2aee1ce'
down_revision = 'b85d15633234'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE OR REPLACE VIEW vw_supported_vendor_tech AS
        SELECT 
        t1.pk,
        t2.name as vendor,
        t3.name as technology
        FROM 
        supported_vendor_tech t1
        INNER JOIN  vendors t2 on t2.pk = t1.vendor_pk 
        INNER JOIN technologies t3 on t3.pk = t1.tech_pk
    
    """)

def downgrade():
    pass
