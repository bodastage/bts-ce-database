"""Create MO views for Huawei 4G

Revision ID: 0588ebb5527a
Revises: 316570e7ecab
Create Date: 2018-05-15 10:33:37.306000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0588ebb5527a'
down_revision = '316570e7ecab'
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