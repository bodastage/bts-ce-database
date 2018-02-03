"""Create managedojects table

Revision ID: 0b7905a9ba5b
Revises: 193b5bf5a615
Create Date: 2018-02-03 23:12:32.524000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '0b7905a9ba5b'
down_revision = '193b5bf5a615'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'managedobjects',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text),
        sa.Column('label', sa.String(200)),
        sa.Column('parent_pk', sa.Integer),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('vendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )
    op.execute('ALTER SEQUENCE  managedobjects_pk_seq RENAME TO seq_managedobjects_pk')


def downgrade():
    op.drop_table('managedobjects')
    op.execute('DROP SEQUENCE seq_managedobjects_pk')
