"""Create MO views for Ericsson 3G

Revision ID: 9dd66b7e34a8
Revises: e8560bf05b12
Create Date: 2018-05-14 08:36:55.730000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9dd66b7e34a8'
down_revision = 'e8560bf05b12'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext


UtranRelation = ReplaceableObject(
    'ericsson_cm_3g."UtranRelation"',
    """
        SELECT
        t1."FileName",
        t1."varDateTime",
        t1."configData_dnPrefix",
        t1."SubNetwork_id",
        t1."SubNetwork_2_id",
        t1."MeContext_id",
        t1."ManagedElement_id",
        t1."RncFunction_id",
        t1."UtranCell_id",
        t1."UtranRelation_id",
        t1."adjacentCell",
        t2."vsDataUtranRelation_id",
        t2."qOffset1sn",
        t2."qOffset2sn",
        t2."loadSharingCandidate",
        t2."selectionPriority",
        t2."frequencyRelationType",
        t2."nodeRelationType",
        t2."hcsSib11Config_hcsPrio",
        t2."hcsSib11Config_qHcs",
        t2."hcsSib11Config_penaltyTime",
        t2."hcsSib11Config_temporaryOffset1",
        t2."hcsSib11Config_temporaryOffset2",
        t2."mobilityRelationType",
        t2."createdBy",
        t2."creationTime"
        FROM
        ericsson_bulkcm."UtranRelation" t1
        INNER JOIN ericsson_bulkcm."vsDataUtranRelation" t2
        ON t1."MeContext_id" = t2."MeContext_id"
        AND t1."UtranCell_id" = t2."UtranCell_id"
        AND t1."SubNetwork_id" = t2."SubNetwork_id"
        AND t1."SubNetwork_2_id" = t2."SubNetwork_2_id"
        AND t1."ManagedElement_id" = t2."ManagedElement_id"
        AND t1."FileName" = t2."FileName"
        AND t1."UtranRelation_id" = t2."UtranRelation_id"
        AND t1."varDateTime" = t2."varDateTime"
        AND t1."configData_dnPrefix" = t2."configData_dnPrefix"
        AND t1."RncFunction_id" = t2."RncFunction_id" 
        """
)


def upgrade():
    op.create_view(UtranRelation)


def downgrade():
    op.drop_view(UtranRelation)
