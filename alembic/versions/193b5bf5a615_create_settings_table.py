"""create settings table

Revision ID: 193b5bf5a615
Revises: 256361a12ea8
Create Date: 2018-02-03 20:49:50.452000

"""
from alembic import op
import sqlalchemy as sa
import datetime
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '193b5bf5a615'
down_revision = '256361a12ea8'
branch_labels = None
depends_on = None


def upgrade():
    settings = op.create_table(
        'settings',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('data_type', sa.String(200)),
        sa.Column('integer_value', sa.Integer),
        sa.Column('float_value', sa.Float),
        sa.Column('string_value', sa.String(200)),
        sa.Column('text_value', sa.Text),
        sa.Column('timestamp_value', sa.TIMESTAMP),
        sa.Column('label', sa.String(200)),
        sa.Column('category_id', sa.String(200)),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )
    op.execute('ALTER SEQUENCE  settings_pk_seq RENAME TO seq_settings_pk')

    op.bulk_insert(settings, [
        {'name': 'cm_dag_schedule_interval', 'data_type': 'string', 'string_value': '0 0 * * *', 'text_value':None,
         'category_id': 'configuration_management', 'label': 'CM ETL Schedule'},
        {'name': 'cm_dag_fuelux_scheduler_value', 'data_type': 'text', 'text_value': '{}', 'string_value':None,
         'category_id': 'configuration_management', 'label':'Fuelux UI Component Value'},
    ])

def downgrade():
    op.drop_table('settings')
