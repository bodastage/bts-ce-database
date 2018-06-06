"""Create ZTE 4G MO views

Revision ID: 9b8666957770
Revises: fe292ef150ae
Create Date: 2018-06-06 09:44:56.546000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b8666957770'
down_revision = 'fe292ef150ae'
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