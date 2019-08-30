"""Create report module migrations

Revision ID: 0c50cea7ffd3
Revises: 0d748b2c0067
Create Date: 2019-02-20 01:26:27.307465

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0c50cea7ffd3'
down_revision = '0d748b2c0067'
branch_labels = None
depends_on = None



def upgrade():

    op.execute("CREATE SCHEMA reports")

    op.create_table(
        'reports',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('query', sa.Text, nullable=False),
        sa.Column('db_connector_pk', sa.Integer),
        sa.Column('options', postgresql.JSON), #JSON
		sa.Column('type', sa.String(50)),
        sa.Column('category_pk', sa.Integer),
		sa.Column('in_built', sa.Boolean),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'reports'
    )

    op.execute('ALTER SEQUENCE  reports.reports_pk_seq RENAME TO seq_reports_pk')

    op.create_table(
        'report_categories',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False, unique=True),
        sa.Column('notes', sa.Text, nullable=False),
		sa.Column('in_built', sa.Boolean),
        sa.Column('parent_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'reports'
    )

    op.execute('ALTER SEQUENCE  reports.report_categories_pk_seq RENAME TO seq_report_categories_pk')

    op.create_table(
        'reports_task_log',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('action', sa.String(200), nullable=False), # reports.generate
        sa.Column('log', sa.Text),
        sa.Column('options', postgresql.JSON),
        sa.Column('status', sa.String(200)), # FAILED,RUNNING,PENDING,STARTED
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'reports'
    )

    op.execute('ALTER SEQUENCE  reports.reports_task_log_pk_seq RENAME TO seq_reports_task_log_pk')

def downgrade():
    op.drop_table('reports', schema=u'reports')
    op.drop_table('report_categories', schema=u'reports')
    op.drop_table('reports_task_log', schema=u'reports')

    op.execute("DROP SCHEMA reports")

