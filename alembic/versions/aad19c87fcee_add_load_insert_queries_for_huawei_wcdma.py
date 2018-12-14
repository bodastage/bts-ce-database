"""add load insert queries for huawei wcdma

Revision ID: aad19c87fcee
Revises: a14e40884a2e
Create Date: 2018-12-03 11:11:25.394475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aad19c87fcee'
down_revision = 'a14e40884a2e'
branch_labels = None
depends_on = None


def upgrade():
    cm_load_insert_queries = sa.sql.table(
        'cm_load_insert_queries',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_cm_load_insert_queries_pk', ), primary_key=True, nullable=False),
        sa.Column('file_format', sa.String(200), nullable=False),
        sa.Column('mo', sa.String(200)),
        sa.Column('format_mo', sa.String(200)),
        sa.Column('insert_query', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now())
    )

    op.bulk_insert(cm_load_insert_queries, [
    ])

def downgrade():
    pass