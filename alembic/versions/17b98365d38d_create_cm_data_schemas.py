"""create cm data schemas

Revision ID: 17b98365d38d
Revises: f2f9e2603531
Create Date: 2018-02-05 15:41:50.237000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17b98365d38d'
down_revision = 'f2f9e2603531'
branch_labels = None
depends_on = None


def upgrade():
    # Ericsson
    op.execute("CREATE SCHEMA ericsson_cm")
    op.execute("CREATE SCHEMA ericsson_bulkcm")
    op.execute("CREATE SCHEMA ericsson_cnaiv2")


    # Huawei
    op.execute("CREATE SCHEMA huawei_cm")
    op.execute("CREATE SCHEMA huawei_gexport")
    op.execute("CREATE SCHEMA huawei_mml")
    op.execute("CREATE SCHEMA huawei_nbi")
    op.execute("CREATE SCHEMA huawei_cfgsyn")
    op.execute("CREATE SCHEMA huawei_rnp") # Radio Network Planning Data Template xlsm

    # ZTE
    op.execute("CREATE SCHEMA zte_cm")
    op.execute("CREATE SCHEMA zte_bulkcm")
    op.execute("CREATE SCHEMA zte_excel")

    # Nokia
    op.execute("CREATE SCHEMA nokia_cm")
    op.execute("CREATE SCHEMA nokia_raml2")


def downgrade():
    op.execute("DROP SCHEMA ericsson_cm")
    op.execute("DROP SCHEMA ericsson_bulkcm")
    op.execute("DROP SCHEMA ericsson_cnaiv2")

    # Huawei
    op.execute("DROP SCHEMA huawei_cm")
    op.execute("DROP SCHEMA huawei_gexport")
    op.execute("DROP SCHEMA huawei_mml")
    op.execute("DROP SCHEMA huawei_nbi")
    op.execute("DROP SCHEMA huawei_cfgsyn")
    op.execute("DROP SCHEMA huawei_rnp")

    # ZTE
    op.execute("DROP SCHEMA zte_cm")
    op.execute("DROP SCHEMA zte_bulkcm")
    op.execute("DROP SCHEMA zte_excel")

    # Nokia
    op.execute("DROP SCHEMA nokia_cm")
    op.execute("DROP SCHEMA nokia_raml2")
