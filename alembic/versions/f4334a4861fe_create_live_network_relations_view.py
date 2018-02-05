"""create live network relations view

Revision ID: f4334a4861fe
Revises: f93f0f1b666b
Create Date: 2018-02-05 13:32:54.534000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4334a4861fe'
down_revision = 'f93f0f1b666b'
branch_labels = None
depends_on = None

def upgrade():
    op.execute("""
        CREATE OR REPLACE VIEW live_network.vw_relations AS
        SELECT t1.pk,
            t4.name AS svrnode,
            t3.name AS svrsite,
            t2.name AS svrcell,
            t5.name AS svrvendor,
            t6.name AS svrtechnology,
            t9.name AS nbrnode,
            t8.name AS nbrsite,
            t7.name AS nbrcell,
            t10.name AS nbrvendor,
            t11.name AS nbrtechnology
        FROM live_network.relations t1
            JOIN live_network.cells t2 ON t2.pk = t1.svrcell_pk
            JOIN live_network.sites t3 ON t3.pk = t1.svrsite_pk
            JOIN live_network.nodes t4 ON t4.pk = t1.svrnode_pk
            JOIN vendors t5 ON t5.pk = t1.svrvendor_pk
            JOIN technologies t6 ON t6.pk = t1.svrtech_pk
            JOIN live_network.cells t7 ON t7.pk = t1.nbrcell_pk
            JOIN live_network.sites t8 ON t8.pk = t1.nbrsite_pk
            JOIN live_network.nodes t9 ON t9.pk = t1.nbrnode_pk
            JOIN vendors t10 ON t10.pk = t1.nbrvendor_pk
            JOIN technologies t11 ON t11.pk = t1.nbrtech_pk
    """)


def downgrade():
    op.execute("""DROP VIEW live_network.vw_relations""")
