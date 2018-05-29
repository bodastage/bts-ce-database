"""Create site parameter baseline audit

Revision ID: 638009709b7e
Revises: 9e01150763bf
Create Date: 2018-03-22 15:38:23.474000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '638009709b7e'
down_revision = '9e01150763bf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'site_parameter_baseline',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('node', sa.String(100), nullable=False),
        sa.Column('site', sa.String(200), nullable=False),
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
    op.execute('ALTER SEQUENCE  network_audit.site_parameter_baseline_pk_seq RENAME TO seq_site_parameter_baseline_pk')

    audit_categories = sa.sql.table(
        'audit_categories',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_audit_categories_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('notes', sa.Text, nullable=False),
        sa.Column('parent_pk', sa.Integer, nullable=False, default=0),
        sa.Column('in_built', sa.Boolean, default=False),
        sa.Column('modified_by', sa.Integer, default=0),
        sa.Column('added_by', sa.Integer, default=0),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )

    audit_rules = sa.sql.table(
        'audit_rules',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_audit_categories_pk', ), primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('notes', sa.Text, nullable=False),
        sa.Column('category_pk', sa.Integer, nullable=False, default=0),
        sa.Column('in_built', sa.Boolean, default=False),
        sa.Column('table_name', sa.String(255), nullable=False),
        sa.Column('sql', sa.Text, nullable=False),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )

    connection = op.get_bind()
    r = connection.execute(audit_categories.select().where(audit_categories.c.name == 'Network Baseline'))

    category_pk = 0
    for row in r:
        category_pk = row['pk']

    op.bulk_insert(audit_rules, [
        {'name': 'Site Parameter Discrepancies', 'category_pk': category_pk, 'in_built': True,
         'table_name': 'site_parameter_baseline',
         'sql': 'SELECT * FROM network_audit.baseline_site_parameters',
         'notes': 'Network Baseline Discrepancies for Site parameters'},


    ])


def downgrade():
    op.drop_table('site_parameter_baseline', schema=u'network_audit')
