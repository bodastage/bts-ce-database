"""Create network entities table

Revision ID: 9e01150763bf
Revises: dd770be0c1f7
Create Date: 2018-03-16 13:37:16.677000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e01150763bf'
down_revision = 'dd770be0c1f7'
branch_labels = None
depends_on = None


def upgrade():
    network_entities = op.create_table(
        'network_entities',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('tech_pk', sa.String(50), nullable=False),
        sa.Column('notes', sa.Text, nullable=False),
        sa.Column('modified_by', sa.Integer, default=0),
        sa.Column('added_by', sa.Integer, default=0),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now())
    )
    op.execute('ALTER SEQUENCE  network_entities_pk_seq RENAME TO seq_network_entities_pk')

    op.bulk_insert(network_entities, [
        {'name': 'Cell', 'tech_pk': 1, 'notes': 'GSM Cell'},
        {'name': 'UCell', 'tech_pk': 2, 'notes': 'UMTS/UTRAN Cell'},
        {'name': 'EUCell', 'tech_pk': 3, 'notes': 'LTE/EUTRAN Cell'},
        {'name': 'BTS', 'tech_pk': 1, 'notes': 'Base Transciever Station '},
        {'name': 'NodeB', 'tech_pk': 2, 'notes': 'UMTS Site'},
        {'name': 'ENodeB', 'tech_pk': 3, 'notes': 'LTE Site'},
        {'name': 'BSC', 'tech_pk': 1, 'notes': 'Base Station Controller'},
        {'name': 'RNC', 'tech_pk': 2, 'notes': 'Radio Network Controller'},
        {'name': 'MSC', 'tech_pk': 1, 'notes': 'Mobile Switching Center'},
        {'name': 'MME', 'tech_pk': 3, 'notes': 'Mobility Management Entity'},
        {'name': 'CG', 'tech_pk': 1, 'notes': 'GSM Cell Channel Group'}
    ])


def downgrade():
    op.drop_table('network_entities')
