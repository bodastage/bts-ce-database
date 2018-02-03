"""create vendors table

Revision ID: b45698c3839b
Revises: 
Create Date: 2018-02-03 03:04:14.816000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b45698c3839b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
op.create_table(
        'vendors',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
		sa.Column('modified_by', sa.Integer),
		sa.Column('added_by', sa.Integer),
		sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
		sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
    )


def downgrade():
    op.drop_table('vendors')
