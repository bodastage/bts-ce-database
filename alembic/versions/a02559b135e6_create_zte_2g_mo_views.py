"""Create ZTE 2G MO views

Revision ID: a02559b135e6
Revises: c681b256e567
Create Date: 2018-06-06 09:42:45.478000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a02559b135e6'
down_revision = 'c681b256e567'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext

def upgrade():
    pass

def downgrade():
    pass