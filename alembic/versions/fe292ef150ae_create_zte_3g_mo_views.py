"""Create ZTE 3G MO views

Revision ID: fe292ef150ae
Revises: a02559b135e6
Create Date: 2018-06-06 09:44:51.752000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe292ef150ae'
down_revision = 'a02559b135e6'
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