"""create live_network schema

Revision ID: 5309f65cfd33
Revises: e83c5549560c
Create Date: 2018-02-05 02:34:16.905000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '5309f65cfd33'
down_revision = 'e83c5549560c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA live_network")

def downgrade():
    op.execute("DROP SCHEMA live_network")
