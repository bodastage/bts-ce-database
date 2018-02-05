"""create table base_line_values

Revision ID: 48071f2cf14b
Revises: 5309f65cfd33
Create Date: 2018-02-05 02:37:30.869000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '48071f2cf14b'
down_revision = '5309f65cfd33'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'base_line_values',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('parameter_pk', sa.Integer, nullable=False),
        sa.Column('value', sa.String(200)),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.base_line_values_pk_seq RENAME TO seq_base_line_values_pk')


def downgrade():
    op.drop_table('base_line_values', schema=u'live_network')
