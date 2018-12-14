"""Create MO views for Ericsson 2G

Revision ID: e36afc666feb
Revises: cb540db6ffbf
Create Date: 2018-05-15 05:37:36.889000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e36afc666feb'
down_revision = 'cb540db6ffbf'
branch_labels = None
depends_on = None



class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext
        self.sqltext = sqltext

def upgrade():
    pass

def downgrade():
    pass