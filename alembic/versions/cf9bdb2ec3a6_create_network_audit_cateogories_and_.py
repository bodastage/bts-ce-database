"""Create network audit cateogories and rules tables

Revision ID: cf9bdb2ec3a6
Revises: b459b9fd49f9
Create Date: 2018-03-14 01:23:32.833000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf9bdb2ec3a6'
down_revision = 'b459b9fd49f9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'audit_categories',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('notes', sa.Text, nullable=False),
        sa.Column('parent_pk', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )
    op.execute('ALTER SEQUENCE  audit_categories_pk_seq RENAME TO seq_audit_categories_pk')

    op.create_table(
        'audit_rules',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('notes', sa.Text, nullable=False),
        sa.Column('category_pk', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )
    op.execute('ALTER SEQUENCE  audit_rules_pk_seq RENAME TO seq_audit_rules_pk')

def downgrade():
    op.drop_table('audit_categories')
    op.drop_table('audit_rules')
