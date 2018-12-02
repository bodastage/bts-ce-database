"""create table for cm load insert queries

Revision ID: 053659c382dc
Revises: a04aac3da46d
Create Date: 2018-12-01 12:46:48.608877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '053659c382dc'
down_revision = 'a04aac3da46d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cm_load_insert_queries',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('file_format', sa.String(200), nullable=False),
        sa.Column('mo', sa.String(200)),
        sa.Column('insert_query', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now())
    )
    op.execute('ALTER SEQUENCE  cm_load_insert_queries_pk_seq RENAME TO seq_cm_load_insert_queries_pk')
    op.create_unique_constraint('unique_cm_load_insert_queries', 'cm_load_insert_queries', ['file_format', 'mo'])


def downgrade():
    op.drop_constraint("unique_cm_load_insert_queries", "cm_load_insert_queries")
    op.drop_table('cm_load_insert_queries')
