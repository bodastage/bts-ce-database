"""Create normalized managed object table

Revision ID: 46c028cee28a
Revises: e36afc666feb
Create Date: 2018-05-15 07:07:48.729000

"""
from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision = '46c028cee28a'
down_revision = 'e36afc666feb'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'normalized_managedobjects',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('label', sa.String(200)),
        sa.Column('parent_pk', sa.Integer),
        sa.Column('affect_level', sa.Integer),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )
    op.execute('ALTER SEQUENCE  normalized_managedobjects_pk_seq RENAME TO seq_normalized_managedobjects_pk')


def downgrade():
    op.drop_table('normalized_managedobjects')
