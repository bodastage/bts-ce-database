"""create live_network cells table

Revision ID: 8579697b2bb6
Revises: 9b3717bc5552
Create Date: 2018-02-05 03:01:26.177000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '8579697b2bb6'
down_revision = '9b3717bc5552'
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
    op.execute('ALTER SEQUENCE  base_line_values_pk_seq RENAME TO seq_base_line_values_pk')


def downgrade():
    pass
