"""Create network definition audits

Revision ID: c681b256e567
Revises: 4609e428f1eb
Create Date: 2018-05-29 13:07:34.841000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c681b256e567'
down_revision = '4609e428f1eb'
branch_labels = None
depends_on = None



def upgrade():
    incosistent_2g_externals = op.create_table(
        'incosistent_2g_externals',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('nodename', sa.String(100), nullable=False),
        sa.Column('ext_vendor', sa.String(100), nullable=False),
        sa.Column('int_vendor', sa.String(100), nullable=False),
        sa.Column('int_cellname', sa.String(200), nullable=False),
        sa.Column('ext_mnc', sa.Integer),
        sa.Column('ext_mcc', sa.Integer),
        sa.Column('ext_bcc', sa.Integer),
        sa.Column('ext_ncc', sa.Integer),
        sa.Column('ext_bcch', sa.Integer),
        sa.Column('ext_lac', sa.Integer),
        sa.Column('int_mnc', sa.Integer),
        sa.Column('int_mcc', sa.Integer),
        sa.Column('int_bcc', sa.Integer),
        sa.Column('int_ncc', sa.Integer),
        sa.Column('int_bcch', sa.Integer),
        sa.Column('int_lac', sa.Integer),
        sa.Column('age', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'network_audit'
    )
    op.execute('ALTER SEQUENCE  network_audit.incosistent_2g_externals_pk_seq RENAME TO seq_incosistent_2g_externals_pk')
    op.create_unique_constraint('unique_incosistent_2g_externals', 'incosistent_2g_externals', \
                                ['nodename','ext_vendor', 'int_vendor','int_cellname','ext_mnc','ext_mcc','ext_bcc', \
                                 'ext_ncc','ext_bcch','ext_lac','int_mnc','int_mcc','int_bcc','int_ncc','int_bcch',\
                                 'int_lac'], schema='network_audit')

    incosistent_3g_externals = op.create_table(
        'incosistent_3g_externals',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('nodename', sa.String(100), nullable=False),
        sa.Column('ext_vendor', sa.String(100), nullable=False),
        sa.Column('int_vendor', sa.String(100), nullable=False),
        sa.Column('ext_cellname', sa.String(100), nullable=False, default=0),
        sa.Column('ext_mnc', sa.Integer),
        sa.Column('ext_mcc', sa.Integer),
        sa.Column('ext_dl_uarfcn', sa.Integer),
        sa.Column('ext_rac', sa.Integer),
        sa.Column('ext_lac', sa.Integer),
        sa.Column('ext_psc', sa.Integer),
        sa.Column('int_mnc', sa.Integer),
        sa.Column('int_mcc', sa.Integer),
        sa.Column('int_dl_uarfcn', sa.Integer),
        sa.Column('int_rac', sa.Integer),
        sa.Column('int_lac', sa.Integer),
        sa.Column('int_psc', sa.Integer),
        sa.Column('age', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'network_audit'
    )
    op.execute('ALTER SEQUENCE  network_audit.incosistent_3g_externals_pk_seq RENAME TO seq_incosistent_3g_externals_pk')
    op.create_unique_constraint('unique_incosistent_3g_externals', 'incosistent_3g_externals', \
                                ['nodename','ext_vendor','int_vendor','ext_cellname','ext_mnc', \
                                 'ext_mcc','ext_dl_uarfcn','ext_rac','ext_lac','ext_psc','int_mnc',\
                                 'int_mcc','int_dl_uarfcn','int_rac','int_lac','int_psc'], schema='network_audit')

    incosistent_4g_externals = op.create_table(
        'incosistent_4g_externals',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('nodename', sa.String(100), nullable=False),
        sa.Column('ext_vendor', sa.String(100), nullable=False),
        sa.Column('int_vendor', sa.String(100), nullable=False),
        sa.Column('ext_cellname', sa.String(100), nullable=False, default=0),
        sa.Column('ext_mnc', sa.Integer),
        sa.Column('ext_mcc', sa.Integer),
        sa.Column('ext_dl_earfcn', sa.Integer),
        sa.Column('ext_pci', sa.Integer),
        sa.Column('int_mnc', sa.Integer),
        sa.Column('int_mcc', sa.Integer),
        sa.Column('int_dl_earfcn', sa.Integer),
        sa.Column('int_pci', sa.Integer),
        sa.Column('age', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'network_audit'
    )
    op.execute('ALTER SEQUENCE  network_audit.incosistent_4g_externals_pk_seq RENAME TO seq_incosistent_4g_externals_pk')
    op.create_unique_constraint('unique_incosistent_4g_externals', 'incosistent_4g_externals', \
                                ['nodename','ext_vendor','int_vendor','ext_cellname','ext_mnc','ext_mcc',\
                                 'ext_dl_earfcn','ext_pci','int_mnc','int_mcc','int_dl_earfcn','int_pci'], \
                                schema='network_audit')

    redundant_externals = op.create_table(
        'redundant_externals',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('nodename', sa.String(100), nullable=False),
        sa.Column('technology', sa.String(100), nullable=False),
        sa.Column('vendor', sa.String(100), nullable=False),
        sa.Column('cellname', sa.String(100), nullable=False, default=0),
        sa.Column('age', sa.Integer, nullable=False, default=0),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'network_audit'
    )
    op.execute('ALTER SEQUENCE  network_audit.redundant_externals_pk_seq RENAME TO seq_redundant_externals_pk')
    op.create_unique_constraint('unique_redundant_externals', 'redundant_externals',\
                                ['nodename','technology','vendor','cellname'], schema='network_audit')


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
        {'name': 'Definitions', 'notes': 'Network Relations Audits'},
    ])

    connection = op.get_bind()
    r = connection.execute(audit_categories.select().where(audit_categories.c.name == 'Definitions'))

    category_pk = 0
    for row in r:
        category_pk = row['pk']

    op.bulk_insert(audit_rules, [
        {'name': 'Inconsistent 2G externals', 'category_pk': category_pk, 'in_built': True,
         'table_name': 'incosistent_2g_externals',
         'sql': 'SELECT * FROM network_audit.incosistent_2g_externals',
         'notes': 'Inconsistent external 2G parameters'},
    ])

    op.bulk_insert(audit_rules, [
        {'name': 'Inconsistent 3G externals', 'category_pk': category_pk, 'in_built': True,
         'table_name': 'incosistent_3g_externals',
         'sql': 'SELECT * FROM network_audit.incosistent_3g_externals',
         'notes': 'Inconsistent external 3G parameters'},
    ])

    op.bulk_insert(audit_rules, [
        {'name': 'Inconsistent 4G externals', 'category_pk': category_pk, 'in_built': True,
         'table_name': 'incosistent_4g_externals',
         'sql': 'SELECT * FROM network_audit.incosistent_4g_externals',
         'notes': 'Inconsistent external 4G parameters'},
    ])

    op.bulk_insert(audit_rules, [
        {'name': 'Redundant Externals', 'category_pk': category_pk, 'in_built': True,
         'table_name': 'redundant_externals',
         'sql': 'SELECT * FROM network_audit.redundant_externals',
         'notes': 'Redundant externals definitions'},
    ])

def downgrade():
    op.drop_unique_constraint("unique_incosistent_2g_externals", "incosistent_2g_externals", schema=u'network_audit')
    op.drop_unique_constraint("unique_incosistent_3g_externals", "incosistent_3g_externals", schema=u'network_audit')
    op.drop_unique_constraint("unique_incosistent_4g_externals", "incosistent_4g_externals", schema=u'network_audit')
    op.drop_unique_constraint("unique_redundant_externals", "redundant_externals", schema=u'network_audit')

    op.drop_table('incosistent_2g_externals', schema=u'network_audit')
    op.drop_table('incosistent_3g_externals', schema=u'network_audit')
    op.drop_table('incosistent_4g_externals', schema=u'network_audit')

    # @TODO: Remove audit rule table entries
