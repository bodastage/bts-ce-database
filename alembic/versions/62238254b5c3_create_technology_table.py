"""create technology table

Revision ID: 62238254b5c3
Revises: 3e7c77602997
Create Date: 2018-02-03 03:26:30.315000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '62238254b5c3'
down_revision = '3e7c77602997'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'technologies',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
    )
    op.execute('ALTER SEQUENCE  technologies_pk_seq RENAME TO seq_technologies_pk')

def downgrade():
    op.drop_table('technologies')
