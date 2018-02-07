"""Create cm file formats

Revision ID: aa8945d542cf
Revises: c367f20f483c
Create Date: 2018-02-05 12:36:37.333000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'aa8945d542cf'
down_revision = 'c367f20f483c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cm_file_formats',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('label', sa.String(100), nullable=False),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer, nullable=False),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
    )
    op.execute('ALTER SEQUENCE  cm_file_formats_pk_seq RENAME TO seq_cm_file_formats_pk')

    cm_file_formats = sa.sql.table(
        'cm_file_formats',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_cm_file_formats_pk', ), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('label', sa.String(100), nullable=False),
        sa.Column('vendor_pk', sa.Integer, nullable=False),
        sa.Column('tech_pk', sa.Integer, nullable=False),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
    )

    op.bulk_insert(cm_file_formats, [
        # Ericsson 2G
        {'name': 'cnai_v1', 'vendor_pk':1, 'label':'CNA V2', 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        # Ericsson 3G
        {'name': 'bulk_cm_xml', 'vendor_pk': 1,  'label':'Bulk CM XML', 'tech_pk': 2, 'modified_by': 0, 'added_by': 0},
        # Ericsson 4G
        {'name': 'bulk_cm_xml', 'vendor_pk': 1, 'label': 'Bulk CM XML', 'tech_pk': 3, 'modified_by': 0, 'added_by': 0},
        # Huawei 2G
        {'name': 'huawei_gexport_xml', 'vendor_pk': 2, 'label': 'Huawei GExport XML', 'tech_pk': 1, 'modified_by': 0, 'added_by': 0},
        # Huawei 3G
        {'name': 'huawei_gexport_xml', 'vendor_pk': 2, 'label': 'Huawei GExport XML', 'tech_pk': 2, 'modified_by': 0,
         'added_by': 0},
        # Huawei 4G
        {'name': 'huawei_gexport_xml', 'vendor_pk': 2, 'label': 'Huawei GExport XML', 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
        # ZTE 2G
        {'name': 'bulk_cm_xml', 'vendor_pk': 3, 'label': 'Bulk CM XML', 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0},
        # ZTE 3G
        {'name': 'bulk_cm_xml', 'vendor_pk': 3, 'label': 'Bulk CM XML', 'tech_pk': 2, 'modified_by': 0,
         'added_by': 0},
        # ZTE 4G
        {'name': 'bulk_cm_xml', 'vendor_pk': 3, 'label': 'Bulk CM XML', 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
        # Nokia 2G
        {'name': 'ram_v1', 'vendor_pk': 4, 'label': 'RAM V1', 'tech_pk': 1, 'modified_by': 0,
         'added_by': 0},
        # Nokia 3G
        {'name': 'ram_v1', 'vendor_pk': 4, 'label': 'RAM V1', 'tech_pk': 2, 'modified_by': 0,
         'added_by': 0},
        # Nokia 4G
        {'name': 'ram_v1', 'vendor_pk': 4, 'label': 'RAM V1', 'tech_pk': 3, 'modified_by': 0,
         'added_by': 0},
    ])

def downgrade():
    op.drop_table('cm_file_formats')