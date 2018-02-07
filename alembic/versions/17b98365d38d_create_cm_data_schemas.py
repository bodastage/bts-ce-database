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
    op.execute("CREATE SCHEMA eri_cm_2g")
    op.execute("CREATE SCHEMA eri_cm_3g4g")

    # Huawei
    op.execute("CREATE SCHEMA hua_cm_2g")
    op.execute("CREATE SCHEMA hua_cm_3g")
    op.execute("CREATE SCHEMA hua_cm_4g")

    # ZTE
    op.execute("CREATE SCHEMA zte_cm_2g")
    op.execute("CREATE SCHEMA zte_cm_3g")
    op.execute("CREATE SCHEMA zte_cm_4g")

    # Nokia
    op.execute("CREATE SCHEMA nok_cm_2g")
    op.execute("CREATE SCHEMA nok_cm_3g")
    op.execute("CREATE SCHEMA nok_cm_4g")

    # Alcatel
    op.execute("CREATE SCHEMA alc_cm_2g")
    op.execute("CREATE SCHEMA alc_cm_3g")
    op.execute("CREATE SCHEMA alc_cm_4g")

    # Samsung
    op.execute("CREATE SCHEMA sam_cm_2g")
    op.execute("CREATE SCHEMA sam_cm_3g")
    op.execute("CREATE SCHEMA sam_cm_4g")

def downgrade():
    # Ericsson
    op.execute("DROP SCHEMA eri_cm_2g")
    op.execute("DROP SCHEMA eri_cm_3g4g")

    # Huawei
    op.execute("DROP SCHEMA hua_cm_2g")
    op.execute("DROP SCHEMA hua_cm_3g")
    op.execute("DROP SCHEMA hua_cm_4g")

    # ZTE
    op.execute("DROP SCHEMA zte_cm_2g")
    op.execute("DROP SCHEMA zte_cm_3g")
    op.execute("DROP SCHEMA zte_cm_4g")

    # Nokia
    op.execute("DROP SCHEMA nok_cm_2g")
    op.execute("DROP SCHEMA nok_cm_3g")
    op.execute("DROP SCHEMA nok_cm_4g")

    # Alcatel
    op.execute("DROP SCHEMA alc_cm_2g")
    op.execute("DROP SCHEMA alc_cm_3g")
    op.execute("DROP SCHEMA alc_cm_4g")

    # Samsung
    op.execute("DROP SCHEMA sam_cm_2g")
    op.execute("DROP SCHEMA sam_cm_3g")
    op.execute("DROP SCHEMA sam_cm_4g")
