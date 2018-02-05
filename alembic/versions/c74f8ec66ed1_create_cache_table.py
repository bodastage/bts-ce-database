"""create cache table

Revision ID: c74f8ec66ed1
Revises: 17b98365d38d
Create Date: 2018-02-05 16:08:23.170000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c74f8ec66ed1'
down_revision = '17b98365d38d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cache',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('data', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )
    op.execute('ALTER SEQUENCE  cache_pk_seq RENAME TO seq_cache_pk')


def downgrade():
    op.drop_table('cache')