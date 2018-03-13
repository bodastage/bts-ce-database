"""Create network audit schema

Revision ID: b459b9fd49f9
Revises: 2f30636c9804
Create Date: 2018-03-14 01:08:15.581000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b459b9fd49f9'
down_revision = '2f30636c9804'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA network_audit")

def downgrade():
    op.execute("DROP SCHEMA network_audit")