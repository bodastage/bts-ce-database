"""Create cm data format schemas for all vendors

Revision ID: 41c8d1841d45
Revises: 9bbf9888ebb4
Create Date: 2018-03-28 03:08:11.070000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41c8d1841d45'
down_revision = '9bbf9888ebb4'
branch_labels = None
depends_on = None


def upgrade():

    # Huawei
    op.execute("CREATE SCHEMA huawei_gexport_gsm")
    op.execute("CREATE SCHEMA huawei_gexport_wcdma")
    op.execute("CREATE SCHEMA huawei_gexport_lte")
    op.execute("CREATE SCHEMA huawei_gexport_cdma")
    op.execute("CREATE SCHEMA huawei_gexport_sran")
    op.execute("CREATE SCHEMA huawei_gexport_other")

    op.execute("CREATE SCHEMA huawei_nbi_gsm")
    op.execute("CREATE SCHEMA huawei_nbi_umts")
    op.execute("CREATE SCHEMA huawei_nbi_lte")
    op.execute("CREATE SCHEMA huawei_nbi_cdma")
    op.execute("CREATE SCHEMA huawei_nbi_sran")
    op.execute("CREATE SCHEMA huawei_nbi_other")

    op.execute("CREATE SCHEMA huawei_mml_gsm")
    op.execute("CREATE SCHEMA huawei_mml_umts")
    op.execute("CREATE SCHEMA huawei_mml_lte")
    op.execute("CREATE SCHEMA huawei_mml_cdma")
    op.execute("CREATE SCHEMA huawei_mml_sran")
    op.execute("CREATE SCHEMA huawei_mml_other")

    op.execute("CREATE SCHEMA huawei_cfgsyn")

    # Ericsson
    op.execute("CREATE SCHEMA ericsson_blkcm_3g4g")
    op.execute("CREATE SCHEMA ericsson_eaw_2g")
    op.execute("CREATE SCHEMA ericsson_cnaiv2_2g")

    #ZTE
    op.execute("CREATE SCHEMA zte_blkcm_gsm")
    op.execute("CREATE SCHEMA zte_blkcm_umts")
    op.execute("CREATE SCHEMA zte_blkcm_lte")

    #Nokia
    op.execute("CREATE SCHEMA nokia_raml2_gsm")
    op.execute("CREATE SCHEMA nokia_raml2_umts")
    op.execute("CREATE SCHEMA nokia_raml2_lte")


def downgrade():
    op.execute("DROP SCHEMA huawei_gexport_gsm")
    op.execute("DROP SCHEMA huawei_gexport_wcdma")
    op.execute("DROP SCHEMA huawei_gexport_lte")
    op.execute("DROP SCHEMA huawei_gexport_cdma")
    op.execute("DROP SCHEMA huawei_gexport_sran")
    op.execute("DROP SCHEMA huawei_gexport_other")

    op.execute("DROP SCHEMA huawei_nbi_gsm")
    op.execute("DROP SCHEMA huawei_nbi_umts")
    op.execute("DROP SCHEMA huawei_nbi_lte")
    op.execute("DROP SCHEMA huawei_nbi_cdma")
    op.execute("DROP SCHEMA huawei_nbi_sran")
    op.execute("DROP SCHEMA huawei_nbi_other")

    op.execute("DROP SCHEMA huawei_mml_gsm")
    op.execute("DROP SCHEMA huawei_mml_umts")
    op.execute("DROP SCHEMA huawei_mml_lte")
    op.execute("DROP SCHEMA huawei_mml_cdma")
    op.execute("DROP SCHEMA huawei_mml_sran")
    op.execute("DROP SCHEMA huawei_mml_other")

    op.execute("DROP SCHEMA huawei_cfgsyn")

    # Ericsson
    op.execute("DROP SCHEMA ericsson_blkcm_3g4g")
    op.execute("DROP SCHEMA ericsson_eaw_2g")
    op.execute("DROP SCHEMA ericsson_cnaiv2_2g")

    #ZTE
    op.execute("DROP SCHEMA zte_blkcm_gsm")
    op.execute("DROP SCHEMA zte_blkcm_umts")
    op.execute("DROP SCHEMA zte_blkcm_lte")

    #Nokia
    op.execute("DROP SCHEMA nokia_raml2_gsm")
    op.execute("DROP SCHEMA nokia_raml2_umts")
    op.execute("DROP SCHEMA nokia_raml2_lte")
