"""Add baseline config view

Revision ID: 48cc5ed97f92
Revises: 9b8666957770
Create Date: 2018-06-21 15:05:22.292000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '48cc5ed97f92'
down_revision = '9b8666957770'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext

vw_baseline_parameter_config = ReplaceableObject(
    'live_network."vw_baseline_parameter_config"',
    """
    SELECT t4.name as vendor, t5.name as technology, t2.name as mo, t3.name as parameter 
    FROM live_network.baseline_parameter_config t1
    inner join 
    managedobjects t2 on t2.pk = t1.mo_pk
    inner join 
    vendor_parameters t3 on t3.pk = t1.parameter_pk
    inner join vendors t4 on t4.pk = t2.vendor_pk
    inner join technologies t5 on t5.pk = t2.tech_pk
    """)


def upgrade():
    op.create_view(vw_baseline_parameter_config)


def downgrade():
    op.drop_view(vw_baseline_parameter_config)
