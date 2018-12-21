"""create live network relations table

Revision ID: f93f0f1b666b
Revises: aa8945d542cf
Create Date: 2018-02-05 13:26:04.816000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'f93f0f1b666b'
down_revision = 'aa8945d542cf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'relations',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('svrnode_pk', sa.Integer),
        sa.Column('svrsite_pk', sa.Integer, nullable=False),
        sa.Column('svrcell_pk', sa.Integer, nullable=False),
        sa.Column('nbrnode_pk', sa.Integer),
        sa.Column('nbrsite_pk', sa.Integer),
        sa.Column('nbrcell_pk', sa.Integer),
        sa.Column('svrtech_pk', sa.Integer),
        sa.Column('nbrtech_pk', sa.Integer),
        sa.Column('svrvendor_pk', sa.Integer),
        sa.Column('nbrvendor_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.relations_pk_seq RENAME TO seq_relations_pk')


def downgrade():
    op.drop_table('relations', schema=u'live_network')
