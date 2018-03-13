"""Create network base line audit table

Revision ID: dd770be0c1f7
Revises: cf9bdb2ec3a6
Create Date: 2018-03-14 01:45:31.486000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd770be0c1f7'
down_revision = 'cf9bdb2ec3a6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'network_baseline',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('node', sa.String(100), nullable=False),
        sa.Column('site', sa.String(200), nullable=False),
        sa.Column('cellname', sa.String(200), nullable=False, default=0),
        sa.Column('mo', sa.String(100), nullable=False, default=0),
        sa.Column('parameter', sa.String(100), nullable=False, default=0),
        sa.Column('bvalue', sa.String(200), nullable=False, default=0),
        sa.Column('nvalue', sa.String(100), nullable=False, default=0),
        sa.Column('vendor', sa.String(100), nullable=False, default=0),
        sa.Column('technology', sa.String(100), nullable=False, default=0),
        sa.Column('age', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'network_audit'
    )
    op.execute('ALTER SEQUENCE  network_audit.network_baseline_pk_seq RENAME TO seq_network_baseline_pk')

    audit_categories = sa.sql.table(
        'audit_categories',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_audit_categories_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('notes', sa.Text, nullable=False),
        sa.Column('parent_pk', sa.Integer, nullable=False, default=0),
        sa.Column('in_built', sa.Boolean, default=False),
        sa.Column('modified_by', sa.Integer,  default=0),
        sa.Column('added_by', sa.Integer,  default=0),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )

    audit_rules = sa.sql.table(
        'audit_rules',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_audit_categories_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('notes', sa.Text, nullable=False),
        sa.Column('category_pk', sa.Integer, nullable=False, default=0),
        sa.Column('in_built', sa.Boolean,default=False),
        sa.Column('table_name', sa.String(255), nullable=False),
        sa.Column('sql', sa.Text, nullable=False),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )

    # Create baseline category
    op.bulk_insert(audit_categories, [
        {'name': 'Network Baseline', 'notes': 'Network Baseline Audits'},
    ])

    connection = op.get_bind()
    r = connection.execute(audit_categories.select().where(audit_categories.c.name == 'Network Baseline'))

    category_pk = 0
    for row in r:
        category_pk = row['pk']

    op.bulk_insert(audit_rules, [
        {'name': 'Baseline Discrepancies', 'category_pk': category_pk, 'in_built': True, 'table_name': 'network_baseline',
         'sql':'SELECT * FROM network_audit.network_baseline', 'notes': 'Network Baseline Discrepancies'},
    ])


def downgrade():
    op.drop_table('network_baseline', schema=u'network_audit')
