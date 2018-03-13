"""Create baseline generation configuration table

Revision ID: 2f30636c9804
Revises: b7e6c02f6dd1
Create Date: 2018-03-13 02:00:05.229000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f30636c9804'
down_revision = 'b7e6c02f6dd1'
branch_labels = None
depends_on = None


def upgrade():
    baseline_parameter_config = op.create_table(
        'baseline_parameter_config',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('mo_pk', sa.Integer, nullable=False),
        sa.Column('parameter_pk', sa.Integer, nullable=False),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
        schema=u'live_network'
    )
    op.execute('ALTER SEQUENCE  live_network.baseline_parameter_config_pk_seq RENAME TO seq_baseline_parameter_config_pk')

    op.bulk_insert(baseline_parameter_config, [
        {'mo_pk': 817, 'parameter_pk': 10129,  'modified_by': 0, 'added_by': 0}, # GCELL-MCC
        {'mo_pk': 817, 'parameter_pk': 10130, 'modified_by': 0, 'added_by': 0},  # GCELL-MNC
        {'mo_pk': 817, 'parameter_pk': 10126, 'modified_by': 0, 'added_by': 0},  # GCELL-HYBHIFREQBANDSUPPORT
        {'mo_pk': 817, 'parameter_pk': 10134, 'modified_by': 0, 'added_by': 0},  # GCELL-PSHPSP
        {'mo_pk': 817, 'parameter_pk': 10135, 'modified_by': 0, 'added_by': 0},  # GCELL-PSLPSVP
    ])


def downgrade():
    op.drop_table('baseline_parameter_config', schema=u'live_network')
