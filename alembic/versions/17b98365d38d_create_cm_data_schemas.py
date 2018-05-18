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
    op.execute("CREATE SCHEMA ericsson_cm_2g")
    op.execute("CREATE SCHEMA ericsson_cm_3g")
    op.execute("CREATE SCHEMA ericsson_cm_4g")
    op.execute("CREATE SCHEMA ericsson_bulkcm")
    op.execute("CREATE SCHEMA ericsson_cnaiv2")


    # Huawei
    op.execute("CREATE SCHEMA huawei_cm_2g")
    op.execute("CREATE SCHEMA huawei_cm_3g")
    op.execute("CREATE SCHEMA huawei_cm_4g")

    # ZTE
    op.execute("CREATE SCHEMA zte_cm_2g")
    op.execute("CREATE SCHEMA zte_cm_3g")
    op.execute("CREATE SCHEMA zte_cm_4g")
    op.execute("CREATE SCHEMA zte_bulkcm_gsm")
    op.execute("CREATE SCHEMA zte_bulkcm_umts")
    op.execute("CREATE SCHEMA zte_bulkcm_lte")

    # Nokia
    op.execute("CREATE SCHEMA nokia_cm_2g")
    op.execute("CREATE SCHEMA nokia_cm_3g")
    op.execute("CREATE SCHEMA nokia_cm_4g")
    op.execute("CREATE SCHEMA nokia_raml2_gsm")
    op.execute("CREATE SCHEMA nokia_raml2_umts")
    op.execute("CREATE SCHEMA nokia_raml2_lte")

    # Alcatel
    op.execute("CREATE SCHEMA alcatel_cm_2g")
    op.execute("CREATE SCHEMA alcatel_cm_3g")
    op.execute("CREATE SCHEMA alcatel_cm_4g")

    # Samsung
    op.execute("CREATE SCHEMA samsung_cm_2g")
    op.execute("CREATE SCHEMA samsung_cm_3g")
    op.execute("CREATE SCHEMA samsung_cm_4g")

def downgrade():
    op.execute("DROP SCHEMA ericsson_cm_2g")
    op.execute("DROP SCHEMA ericsson_cm_3g")
    op.execute("DROP SCHEMA ericsson_cm_4g")
    op.execute("DROP SCHEMA ericsson_bulkcm")
    op.execute("DROP SCHEMA ericsson_cnaiv2")

    # Huawei
    op.execute("DROP SCHEMA huawei_cm_2g")
    op.execute("DROP SCHEMA huawei_cm_3g")
    op.execute("DROP SCHEMA huawei_cm_4g")

    # ZTE
    op.execute("DROP SCHEMA zte_cm_2g")
    op.execute("DROP SCHEMA zte_cm_3g")
    op.execute("DROP SCHEMA zte_cm_4g")
    op.execute("DROP SCHEMA zte_bulkcm_gsm")
    op.execute("DROP SCHEMA zte_bulkcm_umts")
    op.execute("DROP SCHEMA zte_bulkcm_lte")

    # Nokia
    op.execute("DROP SCHEMA nokia_cm_2g")
    op.execute("DROP SCHEMA nokia_cm_3g")
    op.execute("DROP SCHEMA nokia_cm_4g")
    op.execute("DROP SCHEMA nokia_raml2_gsm")
    op.execute("DROP SCHEMA nokia_raml2_umts")
    op.execute("DROP SCHEMA nokia_raml2_lte")

    # Alcatel
    op.execute("DROP SCHEMA alcatel_cm_2g")
    op.execute("DROP SCHEMA alcatel_cm_3g")
    op.execute("DROP SCHEMA alcatel_cm_4g")

    # Samsung
    op.execute("DROP SCHEMA samsung_cm_2g")
    op.execute("DROP SCHEMA samsung_cm_3g")
    op.execute("DROP SCHEMA samsung_cm_4g")
