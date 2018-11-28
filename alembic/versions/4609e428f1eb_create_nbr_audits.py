"""Create NBR audit tables

Revision ID: 4609e428f1eb
Revises: a5ff5b06e303
Create Date: 2018-05-29 09:44:44.930000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4609e428f1eb'
down_revision = 'a5ff5b06e303'
branch_labels = None
depends_on = None


def upgrade():
    missing_one_way_relations = op.create_table(
        'missing_one_way_relations',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('svrvendor', sa.String(100), nullable=False),
        sa.Column('svrtech', sa.String(100), nullable=False),
        sa.Column('svrnode', sa.String(100), nullable=False),
        sa.Column('svrsite', sa.String(200), nullable=False),
        sa.Column('svrcell', sa.String(100), nullable=False, default=0),
        sa.Column('svrnode', sa.String(100), nullable=False),
        sa.Column('nbrvendor', sa.String(100), nullable=False),
        sa.Column('nbrtech', sa.String(100), nullable=False),
        sa.Column('nbrsite', sa.String(200), nullable=False),
        sa.Column('nbrcell', sa.String(100), nullable=False, default=0),
        sa.Column('age', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'network_audit'
    )
    op.execute('ALTER SEQUENCE  network_audit.missing_one_way_relations_pk_seq RENAME TO seq_missing_one_way_relations_pk')
    op.create_unique_constraint('unique_missing_one_way_relations', 'missing_one_way_relations', ['svrvendor', 'svrtech', 'svrnode', 'svrsite', 'svrcell', 'nbrvendor', 'nbrtech', 'nbrsite', 'nbrcell'], schema='network_audit')


    missing_cosite_relations = op.create_table(
        'missing_cosite_relations',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('svrvendor', sa.String(100), nullable=False),
        sa.Column('svrtech', sa.String(100), nullable=False),
        sa.Column('svrnode', sa.String(100), nullable=False),
        sa.Column('svrsite', sa.String(200), nullable=False),
        sa.Column('svrcell', sa.String(100), nullable=False, default=0),
        sa.Column('svrnode', sa.String(100), nullable=False),
        sa.Column('nbrvendor', sa.String(100), nullable=False),
        sa.Column('nbrtech', sa.String(100), nullable=False),
        sa.Column('nbrnode', sa.String(100), nullable=False),
        sa.Column('nbrsite', sa.String(200), nullable=False),
        sa.Column('nbrcell', sa.String(100), nullable=False, default=0),
        sa.Column('age', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'network_audit'
    )
    op.execute('ALTER SEQUENCE  network_audit.missing_cosite_relations_pk_seq RENAME TO seq_missing_cosite_relations_pk')
    op.create_unique_constraint('unique_missing_cosite_relations', 'missing_cosite_relations', \
                                ['svrvendor','svrtech','svrnode','svrsite','svrcell','nbrvendor',\
                                 'nbrtech','nbrnode','nbrsite','nbrcell'], schema='network_audit')


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

    # Create baseline category
    op.bulk_insert(audit_categories, [
        {'name': 'Relations', 'notes': 'Network Relations Audits'},
    ])

    connection = op.get_bind()
    r = connection.execute(audit_categories.select().where(audit_categories.c.name == 'Relations'))

    category_pk = 0
    for row in r:
        category_pk = row['pk']

    op.bulk_insert(audit_rules, [
        {'name': 'Missing one way relations', 'category_pk': category_pk, 'in_built': True,
         'table_name': 'missing_one_way_relations',
         'sql': 'SELECT * FROM network_audit.missing_one_way_relations',
         'notes': 'Missing one way relations'},
    ])

    op.bulk_insert(audit_rules, [
        {'name': 'Missing co-site relations', 'category_pk': category_pk, 'in_built': True,
         'table_name': 'missing_cosite_relations',
         'sql': 'SELECT * FROM network_audit.missing_cosite_relations',
         'notes': 'Missing co-site relations audit'},
    ])


def downgrade():
    op.drop_constraint("unique_missing_one_way_relations", "missing_one_way_relations", schema=u'network_audit')
    op.drop_constraint("unique_unique_missing_cosite_relations", "missing_cosite_relations", schema=u'network_audit')

    op.drop_table('missing_one_way_relations', schema=u'network_audit')
    op.drop_table('missing_cosite_relations', schema=u'network_audit')



    # @TODO: Remove audit rule table entries
