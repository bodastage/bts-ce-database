"""Create supported vendor technology table

Revision ID: b85d15633234
Revises: ed13ecbf37c4
Create Date: 2018-03-02 03:22:38.427000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b85d15633234'
down_revision = 'ed13ecbf37c4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'supported_vendor_tech',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),

    )
    op.execute('ALTER SEQUENCE  supported_vendor_tech_pk_seq RENAME TO seq_supported_vendor_tech_pk')

    op.create_unique_constraint("unq_supported_vendor_tech", "supported_vendor_tech", ["vendor_pk", "tech_pk"])

    supported_vendor_tech = sa.sql.table(
        'supported_vendor_tech',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_supported_vendor_tech_pk', ), primary_key=True, nullable=False),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer, nullable=False),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('date_modified', sa.TIMESTAMP, default=sa.func.now()),
    )

    op.bulk_insert(supported_vendor_tech, [
        {'vendor_pk': 1, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'vendor_pk': 1, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'vendor_pk': 1, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},

        #Huawei - 2g,3,4g
        {'vendor_pk': 2, 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        {'vendor_pk': 2, 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        {'vendor_pk': 2, 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
    ])

def downgrade():
    op.drop_table('supported_vendor_tech')
