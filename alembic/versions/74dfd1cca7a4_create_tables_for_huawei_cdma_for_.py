"""Create tables for Huawei CDMA for GExport format

Revision ID: 74dfd1cca7a4
Revises: 74e93b490a26
Create Date: 2018-04-12 14:52:08.382000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74dfd1cca7a4'
down_revision = '74e93b490a26'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('ACLGRP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ACLRULE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ACTRL_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPRID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('AFABIDICT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('AFABIITEM_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYITEMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ANTIATTACK_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GTPSIGMSGFLOWCTRLSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ANTIVIRUSFUNC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ANTIVIRUSPARA_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VIRUSF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VIRUSNTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VIRUSTTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VUSRPROC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VUSRSMP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('APINFO_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PIPADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIPADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('APPCERT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPCERT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ATMOAMCFG_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACTALARM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACTLIMIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AISLMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCLMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RDILMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BBUFAN_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BFDSESSION_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SESSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BFD_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BFD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BINDGTPCIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GROUPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BINDGTPUIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ITFDRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GROUPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BINDINGCON_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BINDINGCONNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFBINDING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTERFACETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEWBINDINGCONNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USERNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BINDINGRULE_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BINDINGFAILHND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BINDINGRULENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEWBINDINGRULENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAVEORINGINHOST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USEGXSPERRORCODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USERXSPERRORCODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BOARD_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BRDTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SLOTNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRACKNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BRDIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BRD_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADMST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BRDHTYP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FBRDHTYP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('METYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OSUPDTF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BSSAPPTMR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T12_1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T12_2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T6_1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T_WAITALLUSPU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T_WAITALLVLR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BSSGP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BLKCELLTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSIDRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BVCRESETRTYNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLCONGRESTHS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLCONGTHS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLSBVCFLCTRL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CRTPFCRETRY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLOWCTRTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDULFTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIMERCTRPFC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TMRMSFLOW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TMRRESET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('BWRATIO_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STATICBW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CABINET_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CAMELSPT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CUSTSCDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GEMEGCOMB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GESEQPRES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPGPRS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPSMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CAMELTMR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TCGUARD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSSF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CASCADEPORT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CCHARACTER_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESCRIPTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CDRBACKUP_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BACKUPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CKFPASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DELABSPATH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESTSERVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KFPASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LDESTPATH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LDTPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LFILETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LLDTPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LLOGAUDIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSTORDAYS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LTRANSPER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OLDKPASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRCHFI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CDRDISTR_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRDISTRID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CKFPASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPASSWD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KFPASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ODESTPATH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OLDKPASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OTPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUSERNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PARA1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PARA2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PASSWORD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRANSMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CDRPROC_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRPROCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRTIMEOUT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRFNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SEQNUMMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CDRROUTE_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRROUTEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGATEWAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PIPADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PMASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROUTEPURPOSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CDRSTOR_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRSTORID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRINTERV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHLNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLOSEFILECOND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMPTYFILE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FILETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NAMINGRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NUMSCHSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SFCDRSIZE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SFCMRRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SFSTORDAYS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SFSTORDAYSRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STARTSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CDRSYNC_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRSYNCMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CELL_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BVCI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLPRON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLSRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORMAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUTPUTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PTPSTATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CERTCFG_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IKECHECKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CERTCHKTSK_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALMRNG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ISENABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPDATEMETHOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CERTDEPLOY_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEPLOYTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CERTMK_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPCERT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CASW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CERTREQ_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COMMNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KEYSIZE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KEYUSAGE_DATA_ENCIPHERMENT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KEYUSAGE_DIGITAL_SIGNATURE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KEYUSAGE_KEY_AGREEMENT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KEYUSAGE_KEY_ENCIPHERMENT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIGNALG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USERADDINFO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CGEquipment_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CGFunction_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CGMG_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PATHSECENABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CGMODULE_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CGPOMUEquipment_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CGPOMUFunction_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CGSYSRES_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BACKSAVEALL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FRONTSAVEALL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEMALL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHGCDPIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEART', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UDPPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHGCDR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRPLMNSELECT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGPLMNSELECT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CRC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CRQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EXTRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FRCGEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IGNOREFLG_HOME_APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IGNOREFLG_HOME_SUBSCRIBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IGNOREFLG_ROAM_APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IGNOREFLG_ROAM_SUBSCRIBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IGNOREFLG_VISIT_APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IGNOREFLG_VISIT_SUBSCRIBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_CC_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_LCS_PRIOPITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_LOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_LOCATION_ESTIMATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_MEASUREMENT_DURATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_NODE_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_SERVED_MSISDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_SGSN_ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOL_SYSTEM_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_CC_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_LCS_CAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_LOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_LOCATION_ESTIMATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_MEASUREMENT_DURATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_NODE_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_SERVED_MSISDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_SGSN_ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTL_SYSTEM_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_CC_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_LOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_LOCATION_ESTIMATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_MEASUREMENT_DURATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_NODE_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_SERVED_IMEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_SGSN_ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIL_SYSTEM_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LRSNP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_CAMEL_INFO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_CC_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_CELL_PLMN_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_CHANGE_OF_LOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_CI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_DIAGNOSTICS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_DURATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_LAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_MS_NETWORK_CAPABILITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_NODE_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_SERVED_IMEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_SERVED_MSISDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_SGSN_ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ML_SYSTEM_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NONSUPPUEPLMN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLMNCTRL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_APNNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_APNOI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_APN_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_CAMEL_INFO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_CC_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_CELL_PLMN_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_CI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_DAF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_DIAGNOSTICS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_IMSI_UNAUTHENTICATED_FLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_LAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_LIST_OF_TDV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_MS_NETWORK_CAPABILITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_NETWORK_INITIATED_PDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_NODE_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_PDP_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_RECORD_EXTENTIONS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_RNC_UDV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_SERVED_IMEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_SERVED_MSISDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_SERVED_PDP_ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_SERVED_PDP_ADDR_EXT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_SGSN_ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_SYSTEM_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SL_USER_CSG_INFORMATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_CAMEL_INFO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_CC_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_CI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_DEST_NUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_LAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_MS_NETWORK_CAPABILITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_NODE_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_RECORDING_ENTITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_RECORD_EXTENTIONS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_SC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_SERVED_IMEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_SERVED_MSISDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOL_SYSTEM_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_CC_SELECT_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_CI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_LAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_MS_NETWORK_CAPABILITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_NODE_ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_RECORDING_ENTITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_RECORD_EXTENTIONS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_SC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_SERVED_IMEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_SERVED_MSISDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTL_SYSTEM_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHGCG_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GRD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLMNFLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHGCHAR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MLCL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MLCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MPCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MPL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPCMCDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPCSCDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCCL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SLCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SVL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SVP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TARIACCFLG_HOME_USER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TARIACCFLG_ROAM_USER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TARIACCFLG_VISIT_USER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHGGA_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDROVERWRITE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGVER4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGVER5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGVER6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGVER7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGVER9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGVER98', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGVER99', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GAREVUDPCHECK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GASENDUDPCHECK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GCR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HDDETH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HDDFSL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ITVRES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOSVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REDICTFRMMAXOCCRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UCR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHGPLMNCHAR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLMN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMOP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSMTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCSNIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMOP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHGWKDY_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WKDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHK_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENABLEFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CHRCFG_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_CRTBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_DELBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_MODBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_OTHER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_PAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_PDNCON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_PDNDISCON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_RESERVED9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_S1HO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_S1RLS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_SGSPAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_SRVCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_SVR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_SYSCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSFAIL_X2HO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_CRTBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_DELBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_MODBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_OTHER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_PAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_PDNCON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_PDNDISCON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_RESERVED9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_S1HO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_S1RLS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_SGSPAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_SRVCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_SVR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_SYSCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPSSUCC_X2HO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_ACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_DEACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_MODPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_OTHER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_PAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED15', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED16', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_RESERVED9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_SUSPEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANFAIL_SYSCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_ACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_DEACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_MODPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_OTHER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_PAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED15', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED16', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_RESERVED9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_SUSPEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GERANSUCC_SYSCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPTDEVNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_ACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_DEACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_IURLS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_MODPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_OTHER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_PAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RAB_ASSIGN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RELOC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED15', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_RESERVED9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_SUSPEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_SVR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANFAIL_SYSCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_ACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_DEACTPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_IURLS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_MODPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_OTHER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_PAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RAB_ASSIGN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RELOC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED15', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_RESERVED9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_SUSPEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_SVR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UTRANSUCC_SYSCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('COMPATIBILITY_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CORRSUBGBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DNLKADJST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DOADJUST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GNQOSVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GTL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HARP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIMITMBR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MARP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTADJST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOSCRCT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOSMAP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLBCLSMAP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAPI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRVHANDOVER2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRVHANDOVER3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TCADJST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPLKADJST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WTL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CONNECTPLMN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COUNTRYORAREANAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXSMNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NOID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('S5S8TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMSCR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CORE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CPUDR_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CDRID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEVEL1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEVEL2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEVEL3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEVEL4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('CRLPOLICY_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CRLPOLICY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DEVADDR_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVAID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESCRIPTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GDM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASKV6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NPNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NPUMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DEVIP_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTRLMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DFTRT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APRG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPPRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DHCPRELAYSWITCH_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DHCPSW_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DIAMPEERPP_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADJINBSWT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DIAMPEERPPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DIAMPEERPPNEWNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RECONNMETHOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RECONNTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_CX/DX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_DIAMTORADIUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_GX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_GXX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_GY/RO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_GZ/RF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_RADIUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_RX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_S13/S13BIS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_S6A/S6D', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_S6B', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_S9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SH/DH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SLH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SP_BIS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_STA/SWA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SWM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SWX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_SY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REPSPECAUTAG_ZH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSTCONNTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSTCONNTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SENDDWRTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPVIDSWT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VNDID0', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VNDID1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VNDID2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VNDID3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WAITDWATIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WTANSTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DIAMPP_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSNPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DIFPRI_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPCLKPRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OMHIGHPRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OMLOWPRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMFUNC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONGTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONNDETECTNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DIAMPEERRSPTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DWRSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FAILOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSGVERNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RECONNMETHOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RECONNTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WAITANSWERTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WATCHDOGTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMLE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOHSTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LORLMNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMLKS_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DANAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LKSM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LKSNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LKSNAME1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMLKS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LINKSIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LINKSNAM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSSELMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMLNKEX_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNKID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNKNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PHN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMLNK_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LINKIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLIORSER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CROSSIPFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LINKNAM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LINKSIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIPV4_1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIPV4_2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIPV4_1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIPV4_2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROCESSNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROTOTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPINDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SLOTNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRACKNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMPEEREX_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PHN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMPE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPCAP_S13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPCAP_S6A/S6D', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPCAP_SLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONGSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERHTNAM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERNAM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMRT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLEXROUTEFAILACT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCACT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NRTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTRSLTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DMRT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROUTEIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPNAM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ISDEFAULT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REALMNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROUTENAM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSELMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DNSCLTIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DNSS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DNSSNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DNS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNAMESW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DDI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DDS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DISCACHEPURGESW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FAILTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPSORTMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PAUSETM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RCQRYTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RCRSPTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RCUPDTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RCUSEDTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REROUTE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SFT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DRACAPACITY_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAPACITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DSCPMAP_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VLANPRIO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DSCPQOS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AF1QOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AF2QOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EFAF43QOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAPSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NCQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DSCPRMK_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPFPB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DSGNETYPE_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSGNETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('DSGNETYPE_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSGNETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EDRREPORT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH_PROVISIONINGEDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH_RXSIGNALINGEDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH_SIGNALINGEDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH_SUBSCRIBERGROUPEDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORCEEDRSW_FORCEACCOUNTEDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORCEEDRSW_FORCEQUOTASTATUSCHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORCEEDRSW_FORCEQUOTAVALUECHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORCEEDRSW_FORCERULEEDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMM_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GUTIREALLOC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GUTITMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GUTITMRFORDEBUG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOCMPSRCTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOCMPTGTTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOPRETMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOT3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMDTCHTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3413', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3422', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3450', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3460', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3470', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PAGINGDELTA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RCHTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3402', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3412', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3413', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3422', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3450', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3460', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3470', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMSTZ_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMSTZ_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMSTZ_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMSTZ_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMSTZ_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMSTZ_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EMSTZ_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('EQUIPMENT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EQUIPMENTTY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ESN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ESM_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3485', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3486', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3489', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3495', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3485', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3486', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3489', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3495', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSAEBRMOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSAEBRREL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSAEBRSETUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ETHPORT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADMINSTRATIVESTATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MACADDRESS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPERATIONALSTATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTLOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIGNTRANSMEDIA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USERLABEL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ETHPORT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPPROXY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTOCFGFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DUPLEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FERAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FERDT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FIBERSPEEDMATCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RXBCPKTALMCLRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RXBCPKTALMOCRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBT_NAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPEED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FCRULE_PRIORITY_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FCSRVANA_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CMDCODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FILTNM1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FILTNM2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FILTNM3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FILTNM4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEWSRVNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRVFCNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRVNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FCSRVFILT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL1T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL2T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL3T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL4T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAL5T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVPAV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONDTA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FILTNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEWFILTNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FENUMTYPE_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDCHAR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FENUMTYPEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FENUMTYPENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NUMLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FEPLUG_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FEPLUGLOADSTATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPEVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOADFILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPFILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FLOWCTRLBUF_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BVCCONRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BVCCONTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BVCDATQL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BVCSIGQL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSCONRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSCONTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSDATQL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSSIGQL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FLOWCTRL_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLWCTRFLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AARIRAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCRIRAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCRTRAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCRURAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUFLWEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUFLWSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPUMINNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPUTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPUTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDUMINNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDUTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDUTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPUMINNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPUTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPUTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYNRAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FLOWCTRL_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUFLWEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUFLWSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DRUTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DRUTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSGTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSGTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSUTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSUTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLWCTRFLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LDAPTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LDAPTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('FTPCLT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENCRYMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MINDHLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPTSTATEFWL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSLCERTAUTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GBACCAREALST_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AREA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTRLTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDCAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GBARD_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAMELSUB_GPRS_CSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAMELSUB_SMS_CSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CARDTYPE_SIM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CARDTYPE_USIM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTRLTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDCAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GBAUTHCIPH_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSIPRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ATTSAUTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_IMSI_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTER_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTRA_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_LCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PROD_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PTMSI_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PTMSI_SIG_NOMATCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PTMSI_SIG_NOSIG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SMS_MO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SMS_MT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SM_DEA_PDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SM_PDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SYSTEM_CHANGE_INTRA_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENTTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHPERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHSETSNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHSETV2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAFTIMES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CIPHALG_GEA_1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CIPHALG_GEA_2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CIPHALG_GEA_3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GETAUTHADVTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IDRQ', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NCIPH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PREGETAUTHSETS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAUSAUTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SECPLC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('XIDRESET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GBDETACH_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DETACHONREADY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DETACHSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMPDTCHTMOUT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NACTTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ONLINEFOREVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ONLINETIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TMIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GBIPLOCENDPT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GBPAGING_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GBSM_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3385', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3386', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3395', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PFT_USED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM_BSS_PFT_T9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3385', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3386', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3395', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GGSNCHARACT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_CAMEL_CHARGING_INFO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_IMEI_SV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_MS_TIME_ZONE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_MS_TIME_ZONE_DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_PLMN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_RAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_RAT_TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EGCDR_USER_LOCATION_INFO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GNGPPATHVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OTS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRVEXT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOSVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMARTPAGING', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GMM_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DFTQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMDTCHTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSRCHTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3313', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3322', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3350', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3360', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3370', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PAGINGDELTA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRDTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RDTDELTA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RDYTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3302', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3313', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3322', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3350', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3360', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3370', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GPS_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AGL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CABLE_LEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DURATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LONG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POSCHECKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRECISION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WPOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GTPPUB_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DNSGTPCPATHFILTERSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ECHOSIG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GTPEXLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GTPEXT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GTPSUPEXTLIST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCRECOVERYSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OTSIE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PATHDOWNDEASW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PATHVERDETECTSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERRECOVERYSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PNTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POOLSRCPORTSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRVEXT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UDPCHKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('V2EI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GTPUCTRL_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPDPTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FWDSPCSRVEXT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSSTDDT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSSTHDT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPTRCFORPFFLUX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPTSPCSRVEXT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GTRANSPARAGW_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPAGINGTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORWARDMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPCLKPRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPERRFRMSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OAMTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PMAUTOSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAMEPORTFORWARDSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('GTRANSPARA_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPAGINGTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BYPASSSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORWARDMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPERRFRMSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEVEL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LPSCHSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MODELSELECT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OAMTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OMCHSWITCHBACK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ONLYOMIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PMAUTOSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RATECFGTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAMEPORTFORWARDSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VLANID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('HPLMN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXSMNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLMNN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('S5S8TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMSCR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IFIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IKECFG_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IKEKLI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IKEKLT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPSECSBRANDTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPSECSBWAITTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPSECSORANDTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPSECSOWAITTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPSECSWITCHBACK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NATKLI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IMSIGT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSIPRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IMSIHSS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSIPRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HSSRLM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IMSISMCHAR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSIPRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UEACCCAP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPRI2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPRI3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DC2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DC3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESDU2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESDU3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DO2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DO3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EARP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBLOCCHANGE_CELL_UPD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBLOCCHANGE_CN_NODE_CHGD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBLOCCHANGE_RAT_CHGD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBLOCCHANGE_RA_UPD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBRDNLK2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBRDNLK3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBRDNLKEX3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBRUPLK2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBRUPLK3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBRUPLKEX3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IULOCCHANGE_CN_NODE_CHGD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IULOCCHANGE_RAT_CHGD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IULOCCHANGE_RA_UPD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IULOCCHANGE_RNC_CHGD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXSDU2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXSDU3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBRDNLK2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBRDNLK3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBRDNLKEX3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBRUPLK2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBRUPLK3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBRUPLKEX3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MT2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MT3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOS2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOS3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RADIOPRI2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RADIOPRI3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RBER2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RBER3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RC2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RC3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDUER2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDUER3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TC2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TC3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TD2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TD3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('THPRI2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('THPRI3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('INAP_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ASWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUDITTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('INGCHKTSK_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLINGCHKITEM_AUDITLOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLINGCHKITEM_OSFILE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLINGCHKITEM_SERVICECONFIG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLINGCHKITEM_SERVICESOFTWARE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLINGCHKITEM_THIRDPARTY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLINGCHKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLINGCHKTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('INSP_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INSPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INSPV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('INSP_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INSPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INSPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INSPV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('INTERCONNE_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Item', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SoftVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Item', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BOM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLEICode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IssueNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Item', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ManufacturerData', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SoftVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BiosVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IssueNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Item', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LogicVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ManufacturerData', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SoftVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLEICode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IssueNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Item', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ManufacturerData', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SoftVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Item', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SoftVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryBoard_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BiosVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BiosVerEx', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IssueNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Item', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LogicVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ManufacturerData', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SoftVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ManufacturerData', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryFrame_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ManufacturerData', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ModuleNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackFrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVerOutSource_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('sDesc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('sDesc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryHostVer_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVer', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostVerType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('sDesc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryPort_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MacAddr', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Status', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryPort_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SubSlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventoryRack_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfManufacture', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SerialNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Status', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VersionNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DateOfLastService', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('InventorySlot_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotPos', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InventoryUnitType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SourceFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UnitPosition', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitFamilyType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VendorUnitTypeNumber', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPADDR_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPUIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPUMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPADDR_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDRNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDRNAME1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDRTYPEV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPDRPRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPENSFPD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPINTERV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GWDETECT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GWV41', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFMMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV41', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LFCTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASKV41', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETPRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOSFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RFCTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TOSVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPCBASEIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPGUARD_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPLRNSTRICTSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPSPOOFCHKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INVALIDPKTCHKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPSECREPLAYCHKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REDIRECTDOSCHKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPNM_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDRNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPNSVC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSVCI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RIPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPPAIR_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPPORT_EXTEND_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPPORT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPADDRESS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MACADDRESS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ODF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPQOS_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVEDELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPUMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXDELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('METYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MINDELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PKTLOSSRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RDPUMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RECPKTNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SENTPKTNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPRESOURCE_CG',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPRID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPDRPRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPINTERV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPPERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GAIPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GATEWAYIIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPRPURPOSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PNETITFACE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPRT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPRT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSTIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSTMASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEXTHOP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PREF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPSECCFG_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPREALM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IKESAINT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IKESATIO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NATKATM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUTRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUTTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUTTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPV4DNSH_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HSINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDRSECTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOSTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4ADDR8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WEIGHT8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IPVLANPRI_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AF1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AF2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AF3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AF4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IUACCAREALST_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AREA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTRLTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDCAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IUARD_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAMELSUB_GPRS_CSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAMELSUB_SMS_CSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CARDTYPE_SIM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CARDTYPE_USIM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTRLTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IUAUTHCIPH_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSIPRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ATTSAUTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_IMSI_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTER_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTER_RAU_AFTER_RELOCATOIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTRA_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTRA_RAU_AFTER_RELOCATOIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_LCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_MS_SERVICE_REQ', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PAGING_RSP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PROD_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PTMSI_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PTMSI_SIG_NOMATCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PTMSI_SIG_NOSIG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SMS_MO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SMS_MT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SYSTEM_CHANGE_INTRA_RAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENTTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHPERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHSETSNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHSETV2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAFTIMES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CIPHALG_NO_ENCRYPTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CIPHALG_UEA1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CIPHALG_UEA2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GETAUTHADVTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IDRQ', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTALG_UIA1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTALG_UIA2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PREGETAUTHSETS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAUSAUTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REAUTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SECPLC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IUDETACH_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DETACHONCONN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DETACHONFOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DETACHSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMPDTCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMPDTCHNORSP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMPIUONNONACT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMPONIUREL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NACTTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NACTTMRONCONN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ONLINEFOREVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ONLINETIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REATM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IULOAD_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IUSHSPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OVERLOADTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IUPAGING_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('IUSM_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3385', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3386', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3395', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3385', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3386', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3395', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LAIVLR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BGNLAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VLRNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DFLVLR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDLAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LDSMR_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LDFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTERVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STRTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LICCTRL_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LICENSEINFO_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAX2GSUB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAX3GSUB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXACT2GPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXACT3GPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXCOMMPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXCOMMSUB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXLAWFULNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LICRATE_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACTVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXSESSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USEDRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LINKTYPE_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SERVICETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LLDPGLOBAL_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOLDMULTI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NOTIFYINTERVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NOTIFYSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REINITDELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TXINTVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LN_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IN2S', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NLNN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NN2S', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NNS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LOCALETHPORT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GRATUITOUSARPSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LOCALIP_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LOCALNRI_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NRIVBGN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POOLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NRINUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LOCALPARA_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPC14FMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPC24FMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGIFMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSCIDFMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('LOCATION_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('M3DE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADJF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SLSSM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('M3LE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('M3LKS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SLSM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('M3LNK_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ASF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONETHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONSTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CROSSIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LKN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPINDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('M3RT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MANRESALMRPT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MAPFUNC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EIR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SEG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MBMSBRRES_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBMSBCOThr', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBMSBCThr', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBMSBNum', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MEPROCESS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROCNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROCTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ME_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SNID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEIID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MELN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEPATCHVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('METYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEVD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MMEID_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMEC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMEGI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMECNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MMFUNC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AREADECRYPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOIEPLY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_INTER_MME_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_INTER_RAT_INTER_USN_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_INTER_RAT_INTRA_USN_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_INTRA_MME_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_PERIOD_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_TAU_AFTER_INTER_MME_HANDOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_TAU_AFTER_INTER_RAT_INTER_USN_HANDOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_TAU_AFTER_INTER_RAT_INTRA_USN_HANDOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMMINFOSENDPLY_TAU_AFTER_INTRA_MME_HANDOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENRAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORBIDTA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LASTTA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCRPTTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMINFO_GB_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMINFO_IU_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMINFO_S1_MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NOIDCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QCIPAGINGSUPPORTED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RANBASEDSHARE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TALIST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MODULE_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADMST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LODMOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MTP3BTMR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q707_T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q707_T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T17', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T22', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T23', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MTP3TMR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q707_T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q707_T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T22', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T23', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MVNOFUN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNOID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CMP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MVNONET_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNOMCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNOMNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNOCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNOID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MVNORES_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNOID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GMSHTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GMSLTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GMSNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GPDPHTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GPDPLTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GPDPNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAESHTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAESLTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAESNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBRHTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBRLTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBRNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UMSHTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UMSLTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UMSNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPDPHTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPDPLTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPDPNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('MVNO_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNOID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('N7ALMT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALMNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L1IC_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L1I_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L1OC_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L1O_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L2IC_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L2I_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L2OC_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('L2O_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNKBSC_LOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NALMNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NEMNT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNTMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NE_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLOUDBBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTERFACEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LMTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NERMVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRODUCTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NODE_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTERFACEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LMTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LTEMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NERMVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRODUCTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRODUCTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NOTIFYCFG_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMOTEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INFTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCATIONID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RESENDTIMES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYNCHROSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WAITTIMEOUT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NSE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CBL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLUSTHT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GB-FLEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OTHERNODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PFC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RACAP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RIM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SGSNINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPECSRV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALIVERTYNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ATNSEDIS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BLOCKRTYNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BLOCKTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEFTDELLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSERPTRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROVRTYNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROVTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSTRTYNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSTTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSTTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UNBLOCKRTYNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NTPCLIENTIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('NTPCP_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('KEYID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASTERFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYNCCYCLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('OFFLOADINF_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FIRSTTM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FOLLOWONPROCEED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORCETOSTANDBY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NONRAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OFFLOADTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('OMCH_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEAR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHECKTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLAG_NAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERMASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('OPC_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP2C', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEWOPCNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NP2C', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPCNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('OP_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCKST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWOP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('OSPF_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PAGINGRULE4STAT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RULEDESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RULEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PAIREDBOARDS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PCEFABIDICT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PCEFABIITEM_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYITEMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABLITYVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PDHOSTCFG_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOSTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DHN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCEFCAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPCEFGROUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PDPAPN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PDPCAR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BURSTTIMES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPMULTI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PDREALMCFG_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REALMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ABILITYDICTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCEFCAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PDU_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDUID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDURN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PEERL_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNKID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADSTS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CROSSPATH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DISPMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DUALHOME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LPTMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPUMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PEERPLMN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AREA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPLMN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPLMN2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPLMN3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EPLMN4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PERFAPN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PEU_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PFBW_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PFBFB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PFBT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PFRES_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BWCTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BWNTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BWOTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BWRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUBTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUCTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPULSSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUNTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPURTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FBWCTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GPRSSELCPUTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTRM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPPOLICY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPSCRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPSCTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPSOLRHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPSOLTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPTF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPTF3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRSELECT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PGWFLOWCTRL_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGWCPUFLWEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGWCPUFLWSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGWFCCPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGWFLWCTRFLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGWSYSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGWTSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PGWTSSTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PHYPORT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADMINISTRATIVESTATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PMGRPORT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALIVETIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENABLEPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PMM_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMDTCHTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSRCHTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3313', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3322', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3350', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3360', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('N3370', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PAGINGDELTA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRDTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RELIUTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLCNEW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLCOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLCTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3302', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3313', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3322', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3350', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3360', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('T3370', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PMSCFG_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ITEMN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PMSNTFCFG_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACTNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('POOLNRI_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NRIV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POOLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SGSNN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('POOL_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POOLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NRILENGTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PORTIPPOOL_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTIPPOOLNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTIPBEGIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTIPEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTIPMASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PORTPOLICY_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USBACCESSSECPOLICY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PORT_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EXPECTWORKMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OAMST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WORKMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PORT_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DISABLEPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HEADERAUTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTBUSSTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PORTTYPENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RETURNHEADER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PPCEFCAT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCEFCATID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ISAPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCEFCAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TERMINALPROCESS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIMEOUTPROCESS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_ACCESS_NETWORK_INFO_REPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_AN_GW_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_APPLICATION_START', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_APPLICATION_STOP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_CHARGING_CORRELATION_EXCHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_CS_TO_PS_HANDOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_DEFAULT_EPS_BEARER_QOS_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_ECGI_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_GW_PCEF_MALFUNCTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_LOSS_OF_BEARER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_MAX_NR_BEARERS_REACHED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_NO_EVENT_TRIGGERS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_OUT_OF_CREDIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_PLMN_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_QOS_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_QOS_CHANGE_EXCEEDING_AUTHORIZATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_RAI_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_RAT_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_REALLOCATION_OF_CREDIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_RECOVERY_OF_BEARER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_RESOURCES_LIMITATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_REVALIDATION_TIMEOUT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_SGSN_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_SUCCESSFUL_RESOURCE_ALLOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_TAI_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_TFT_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_UE_TIME_ZONE_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_USAGE_REPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY1_USER_LOCATION_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_CELL_CLEAR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_CELL_CONGESTED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_DEFAULT_QOS_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_REDIRECTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_SERVICE_FLOW_DETECTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_SUBNET_CHANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_TETHERING_REPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_TFT_DELETED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRIGGERABILITY2_USAGE_THRESHOLD_REACHED', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSAFAILDPROCESS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PRBLIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPPRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PRBPEER_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MFT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PRBSW_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PREALMRT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ISDFT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PRI2QUE_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI0', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PROCESSGRP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROCGRP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PSRVCFG_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSRVID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CFGTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSRVNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PUBLICAPNNI_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PUBNWIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPPRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('PWDPOLICY_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTOUNLOCKTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COMPLICACY_DIGIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COMPLICACY_LOWERCASE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COMPLICACY_SPECHAR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COMPLICACY_UPPERCASE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DICTCHKPWD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FirstLoginMustModPWD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXCCUN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXMISSTIMES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXPERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXREPEATCHARTIMES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MINPERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PASSREPLMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PWDEXPRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PWDMINLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RESETINTERVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('QOSDSCP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BCDSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCDSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ICTHP1DSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ICTHP2DSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ICTHP3DSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAPSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCDSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RACK_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COLNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POSNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROWNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RADIUSPP_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACCESSPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACCOUNTPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RAID_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAIDID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BAKIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RESOURCE_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RESID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RESVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RIPTIMER_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RLOCATION_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RNC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALTBRTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGSYMTOASYMBI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV6ATTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IU-FLEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OTS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('R7QOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RABQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RANSHR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCMCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCMNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SENDRESET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SNDOVERLOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIGOC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TINTC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRABASSGT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRAFR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRATR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UESBI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RTDHOST_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESTHOST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEXTINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEXTRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RTENT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLEXROUTEENTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEXTINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEXTRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NFLEXROUTEENTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RTEXIT_SMNM_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RTEXIT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTRESULT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTRSLTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('RTRESULT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD17', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD18', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD19', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD20', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD21', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD22', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD23', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD24', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD25', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD26', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD27', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD28', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD29', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD30', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD31', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD32', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD33', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD34', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD35', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD36', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD37', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD38', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD39', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD40', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD41', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD42', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD43', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD44', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD45', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD46', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD47', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD48', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD49', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD50', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD51', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD52', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD53', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD54', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD55', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD56', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD57', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD58', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD59', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD60', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD61', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD62', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD63', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRD64', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV15', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV16', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIRLDEV9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROTOCOLTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLDEV1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLDEV2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLDEV3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLDEV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLDEV5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RLSMOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTRSLTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('S1ACCAREALST_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AREA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTRLTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDCAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('S1APLE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LLEINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CROSSIPFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LLNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIPV4_1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIPV4_2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('S1APPARA_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BUNDLETIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BUNDLETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPPLC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMECFGCNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RESTRNSCONTROL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSTCNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIMETOWAIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRMMECFG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSCTPDOWN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSTUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('S1ARD_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAUSE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CTRLTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDIMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('S1USRSECPARA_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSIPRE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_ATTACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_DETACH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTER_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTER_TAU_AFTER_HANDOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTRA_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_INTRA_TAU_AFTER_HANDOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_PROD_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SERVICE_REQUEST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENT_SYSTEM_CHANGE_INTRA_TAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHEVENTTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHPERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHSETSNUMBER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPTIONAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PREGETAUTHSETS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SECPLC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTCIPHAGTH_EEA0', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTCIPHAGTH_EEA1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTCIPHAGTH_EEA2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTCIPHAGTH_EEA3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTINTAGTH_EIA0', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTINTAGTH_EIA1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTINTAGTH_EIA2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPTINTAGTH_EIA3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCANPARA_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSTRTIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SINTERVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCANSW_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCCPDPC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SS7T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCCPEXT_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPCNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCCPGT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GTX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDREXP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GTEXP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCCPOPC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SGSNN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCCPSSN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOADSHARETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSNNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSNX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCCPTMR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TCONNEST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TCOORDCHG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TEA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TFREEZEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TGUARD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIAR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIAS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIGNORESST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TINTERVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TLRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TREASSEMBLY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TREL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TREPEATREL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRESET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRESOURCE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TSTATINFO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCTPASPEERADDR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMOTEIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMOTEIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMOTEPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCTPCFG_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNKNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCTPPARA_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPPARAINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BINDTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHKSUMRX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHKSUMTX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHKSUMTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNGLEVELHIGH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNGLEVELLOW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNGLEVELNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DELAYTMRLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HBINTERVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4MTU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV6MTU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXASSOCRETR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXINSTREAMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXOUTSTREAMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXPATHRETR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MINRECVPKGNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PKGERRFAULT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PKGERRRECOVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTOALPHA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTOBETA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTOINIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTOMAX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RTOMIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPPARANAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SCTPPP_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVEACKNOWLEDG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AVEDEVIATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BUNDLINGFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHECKQUALITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHECKSUMTYP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONGESTTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('COOKIELIFE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DMBUNDLINGFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HEARTBEAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HIGHCONGESTLV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INSPECTFREQ', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INSPECTPER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXCOUPSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXINFLOW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXINITSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXOUTFLOW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXPATHSEND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NOCONGESTTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OLOADENDTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OLOADTHRESHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PARANAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PARANAME1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOSFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RALPHAFACTOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RBETAFACTOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RETRANRATIO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RINITVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RMAXVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RMINVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROUTEMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SACKDATANUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SACKDELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TOSVALUE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SDBTMR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTERPTMSILOCKTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PURGTMR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIPUTME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USPUTME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SEQCHK_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SFP_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MODULEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SGSNCHARACT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GNPATHVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QOSVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPPORTRATIE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SIGATTR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSAPPF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSAPPNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSAPPNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAPNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IRF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3UASTPF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAPNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3BRSTF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3BSTPF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3RSTF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3STPF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NRF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SS7T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SLOT_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SMFUNC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNOIPLY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNRES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DUALFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INDFWD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPRMD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SGWTOPO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TOPSELCFG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TZININTERRAU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SMS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSMSCT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMSMRT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMSODBSCHEME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TR1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TR2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TR3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TR4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SNDCP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DCP0', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DCP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DCP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DMC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXNPDU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSAPIMAXNPDU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PMC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RFC1144CONTEXTNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RFC2507CONTEXTSIZE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RFC2507NONTCPCONTEXTNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RFC2507TCPCONTEXTNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TDCE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TPCE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UNSENTVL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SOAPPP_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSNPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SPSV3DA_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DANAME1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3DANAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3DN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3HN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SPSV3DMLNK_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDRID1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADDRID2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LKSNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LNKNAME1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PIP41', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PIP42', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REGPORTFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPPARANAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3LNKNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SPSV3DMPEER_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BINDINGFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_CX/DX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_GX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_GXX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_GY/RO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_GZ/RF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT22', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT23', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT24', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT25', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT26', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT27', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT28', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT29', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT30', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT31', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RSVBIT32', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_RX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_S13/S13BIS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_S6A/S6D', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_S6B', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_S9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SH/DH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SLH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SP_BIS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_STA/SWA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SWM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SWX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_SY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEVTP_ZH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DIAMPEERPPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FCINSWT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FCOUTSWT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSIMAP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INFCREF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INFCTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INMDENTNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEDSETRM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MEDSETSM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUTFCREF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUTFCTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OUTMDENTNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERTIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RPLNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCONSWT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SHAREKEY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SHAREKEY1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_ISDA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_ISTREQDH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MDA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MDPD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MODANSOH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MODANSOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MODREQDH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MODREQDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MODREQOH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_MODREQOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_NCPF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_NRRBUSY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_NRRNAVA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_RMVQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPM_RSPD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3DMPEERNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIMEOUTPLC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TOPHIDETAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SPSV3FCRULE_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FCRULE1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3FCPRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3FCRULE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SPSV3MODULE_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3MID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3MNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3MT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3SN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPSV3SRN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SPSV3TimeZone_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SSL_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTHMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONNTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOWESTCSLEVEL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RENEGO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RENEGOINTERVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION_SSLV3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION_TLSV10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION_TLSV11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION_TLSV12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('STCFLOWCTRL_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CMDCOUNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SUBDATA_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GROUPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SUBIF_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SUBRACK_CGPOMU',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REFERABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SBVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRMUSN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRMUSN2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRNNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWBBRDT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWFBRDT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SUBRACK_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SYSCAP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBMAXPKTSTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GBMAXTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GNMAXPKTSTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GNMAXTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXPKTSTHPUT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXTHPUT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SYSINFO_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ATTACHNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONTEXTNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCHVOL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('SYS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSFUNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TAIGROUP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TAIGROUPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TAIGROUPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TAILAI_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BGNTAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUBRANGE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENDTAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TAI_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TAKEOVER_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SERVICETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TALST_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TALISTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TASM_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALGORITHM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLKSRC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLKSYNCMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLOUDSRC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENSYSCLKCHKSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FNRECOVERYSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FRAMESYNCSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FREECOUNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOLDCOUNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCKCOUNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PERIOD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAMPLETIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SEARCHCOUNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRCNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYNMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCLKMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCLKSRC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TDFROUTE_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROUTEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROUTEKEY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROUTETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TDFRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TIMER_SPSV3',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONGESTREP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2CIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2CSST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2RCT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2SBIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2T4E', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2T4N', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2T7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2TT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2WDST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M2WSET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3ASPM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3DAUD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3HB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3PD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3RC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3T4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3T8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NTNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PWRONWAIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T41', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T42', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q703_T7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T15', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T16', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T17', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T18', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T19', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T20', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T21', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T22', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T23', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T24', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q704_T9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q707_T1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Q707_T2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ROL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSTWAIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STAAPP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STACHK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STAREP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWAPMONITOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TIMESRC_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTOSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIMESRC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TIMESTRFMT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FMTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FORMAT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TIMETHRD_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('THRD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TLFRSWITCH_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TLFRSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TRUSTCERT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CERTNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TZ_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SMONTH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('TZ_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ZONET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UEFU_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UETYPE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGTP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ICI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PATHVERCHKINT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWAPNPGW_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWAPN_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWBoard_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Type', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('status', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWCG_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGPort', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWCPU_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BoardNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPUID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWDRA_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('hostName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWEPSNSCTPASSOC_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AdministrativeState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OperationalState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWEPSNSPUINSTANCE_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPUInstance', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Board', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWEquipment_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWFrame_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('frameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('InRack', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RackNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWFunction_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWHPLMN_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCCMNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWIpAddrTable_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UGWIpAddrTableId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWIpRouteTable_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UGWIpRouteTableId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWIpTransTable_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UGWIpTransTableId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWNORTH_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxPdpContextNum', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxThroughput', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UserLabela', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UserLabelh', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWOCS_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HostName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPCRFHOST_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('hostName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPCRF_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PcrfIp', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PcrfHost', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PcrfName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PcrfRealm', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPGWFUNCTION_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DiameterIdentity', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxThroughput', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PgwMaxBearers', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UserLabelPgw', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPHGWDOMAIN_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DOMAIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV4AddressAllocate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV6AddressAllocate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('lock', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('radiusServerGroupName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('userProfileGroupName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPHGWPOOL_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('poolName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AddrSegList', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('poolIPType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('poolLock', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('poolType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPHYPORTPGW_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AdministrativeState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EnumPortType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MacAddress', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxThroughput', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OperationalState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortAddress', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortText', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SignTransMedia', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPHYPORTSGW_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AdministrativeState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EnumPortType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MacAddress', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxThroughput', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OperationalState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortAddress', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortText', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SignTransMedia', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPHYPORT_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AdministrativeState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EnumPortType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MacAddress', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxThroughput', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OperationalState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortAddress', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortText', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SignTransMedia', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPoolPGW_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POOLNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNADDRPOOLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGINIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SEGLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPool_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POOLNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APNADDRPOOLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BEGINIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SEGLEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWPRODUCTTYPE_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('productType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWRADIUSAAA_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RADIUSServerIPAddress', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWSCTPASSOC_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AdministrativeState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OperationalState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWSERVICEINSTANCE_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('serviceStatisticName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('dnsStatistic', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('httpStatistic', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('priority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWSGWFUNCTION_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxThroughput', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SgwMaxBearers', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UserLabelSgw', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PlmnIdList', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SgwId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWSPUINSTANCE_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPUInstance', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWTGWAPN_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWTGWDOMAIN_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DOMAIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWTGWSPUINSTANCE_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPUInstance', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Board', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWTUNNEL_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TunnelInterface', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TunnelPHY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TunnelProtocol', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UGWVER_UGW',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CurVersion', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('omcMoName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('parentMoIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('ULPU_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCBOARD_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSLOT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSUBRACK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCEquipment_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCETHPORT_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCNP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSLOT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSUBRACK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCNPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCNPRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCFunction_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCIPADDR_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCIPADDRDPUMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSCP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCETH1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCETH2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCGATEWAYTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCGW1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCGW2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCMASK1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCMASK2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCLOCATION_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCMODULEEX_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCMODULE_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MSTATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCMN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSRN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCPCRF_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCGXTPS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCHN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCPDIAML_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCLNKID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPEERID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPEERTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCPDIAMP_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPEERID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPEERTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCPEER_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPCRFID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPEERID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLSMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDASWITCH_GXON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDASWITCH_GXXON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDASWITCH_RXON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDASWITCH_SDON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDASWITCH_SYON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDATIME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCDN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCHN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCSKA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCWORKMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCPMSLINKCFG_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCLINKID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADSTS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEFLINK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FTPPATH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LINKGRP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALROLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGONINTVAL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MD5CHK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSRVID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USRNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCRDSG_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCRDSGMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCRLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCRIPADDR_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCRLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCRLOCATION_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCRLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCLP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPCCRMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('UPCCSCTPASSOC_UPCC',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USB_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBCLUSTER_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBDATATYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBROLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBSERVICETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBDSGSCTPPARA_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LINKMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBBUNDINGFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCHKSUMRX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCHKSUMTX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCHKSUMTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCNGLEVELH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCNGLEVELL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCNGLEVELNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCONGESTIONFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCOOKIELIFE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBHBINTER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBINITMAXRETR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMAXARETR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMAXNUMASSOC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMAXPRETR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRTOALPHA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRTOBETA', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRTOINIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRTOMAX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRTOMIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBSERVICEPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBTOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBEquipment_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBETHPORT_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBNP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBSLOT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBSUBRACK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NPNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NPRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PEERPOSTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBFunction_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBIPADDR_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBDPUMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPDETECT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPDRPRATE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARPINTERV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT0', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPQOSVALUE_BIT7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LFC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LFCHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RFC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RFCHOLD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SDPUDETECT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBETH1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBGATEWAYTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBGW1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMASK1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBMODULE_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBSERVICETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBSN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBSRN1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBNODE_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBNID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBNORTHFUNC_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBNORTHOBJECTCMC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBPROVSTATOBJ_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBPROVSTATOBJID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBPROVSTATOBJNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBRDSG_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RDSGST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRDSGMID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBRIPADDR_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RDPUST', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBRLOCATION_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRLOCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBRMT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REDUNFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBLP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBSCTPASSOC_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBOBJECTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCALPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMOTEIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMOTEIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMOTEPORT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBSTRNG_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBNETTYP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBOBJECTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NPRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBHLRSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USCDBTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USCDBSUBSCRIBER_USCDB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USN2GPAGING_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIGSlotNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIGSubNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USN3GPAGING_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNBFDSESSION_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FrameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SessionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SlotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APRG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BFDSessionNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PeerIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PortNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNBSSID_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SGSNINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ARP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSCode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSQOSVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CBL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLUSTHT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GB-FLEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LCS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOCN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OTHERNODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PFC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RACAP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RIM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPECSRV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNCG_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CGProRlease', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLMNFLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Priority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNDNSServer_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DNSAddr', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DNSSNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GRPID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNEquipment_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNFunction_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNIFIP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPPRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('frameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ipAddr', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('portNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('slotNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('mask', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNIMSIGT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNIPNSVC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LIPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSVCI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RIPV4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RUP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NSEI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRON', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('frameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('slotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNIPRoute_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPPRO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('routeDestIpAddr', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('routeDestMask', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('routeNextHop', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('routePriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNLicense_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Max2G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAX2GPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAX3GPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAX4GSUB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXCOMMPDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXCOMMSUB', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXINTER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXLINK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Max3G', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('USERMAXCAPCITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNM3UADE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('index', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADJF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DECode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SLSSM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNM3UALE_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('index', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LECode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LEType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NetworkIndicator', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNM3UALinkSet_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('index', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DEIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SLSM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TrafficMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNM3UALink_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('frameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('linkNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('slotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ASF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONETHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CONSTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CROSSIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EXCHGMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LSX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocPort', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PeerIP1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PeerIP2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PeerPort', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCTPINDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('linkName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNMVNO_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MVNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('S5S8TYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNRNCInfo_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ALTBRTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CHGSYMTOASYMBI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IMS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPV6ATTR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IU-FLEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OTS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('R7QOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RABQOS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RANSHR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RNCVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RncName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SENDRESET', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SGSNBUF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SNDOVERLOAD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIGOC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TINTC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRABASSGT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRAFR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRATR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UESBI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNSCCPOPC_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OSNAM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OSNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNSCCPSignallingPoint_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DpcIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LDP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SS7T', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNSCCPSSN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SsnIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOADSHARETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSNNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNSIGATTR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSAPPF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSAPPNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BSSAPPNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAPNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTBFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('M3UASTPF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAPNI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3BEN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3BRSTF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3EN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MTP3RSTF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NATBFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NATFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SS7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNSYSCAP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxGPRSRate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxGPRSGbPackRate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxGPRSGbRate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxGPRSGn_GpPackRate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxGPRSGn_GpRate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxGPRSPackRate', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNSYSInfo_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Switchingvolume', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxNumOfContext', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MaxNumOfUser', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Versioninfo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNSYS_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CAP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PROVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PTMSIALCSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSFUNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSI', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SystemDesc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SystemLoc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('systemName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNVLAN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('frameNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('port', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('slotNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('vlanNo', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USNVLR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MINV', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MOSR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SVSGS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VNM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USRATTR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IULNKTYPE_IU_OVER_ATM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IULNKTYPE_IU_OVER_IP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RESTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPPGTPU', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('USRPDPCAP_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPBRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPBTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPCRTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PDPCTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SCOPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('VLANMAP_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MASK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEXTHOPIP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SETPRIO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VLANID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VLANMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('VLANPORT_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('VLAN_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IFTP', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('VLR_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VLRNO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('VRF_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VRFIDX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('WEBLMT_USU3910',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POLICY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSLVER_SSLV3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSLVER_TLSV10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSLVER_TLSV11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSLVER_TLSV12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

    op.create_table('WRED_USN',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HLVL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LLVL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_cdma'
    )

def downgrade():
    op.drop_table('ACLGRP_USN', schema='huawei_gexport_cdma')
    op.drop_table('ACLRULE_USN', schema='huawei_gexport_cdma')
    op.drop_table('ACTRL_CG', schema='huawei_gexport_cdma')
    op.drop_table('AFABIDICT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('AFABIITEM_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('ANTIATTACK_USN', schema='huawei_gexport_cdma')
    op.drop_table('ANTIVIRUSFUNC_USN', schema='huawei_gexport_cdma')
    op.drop_table('ANTIVIRUSPARA_USN', schema='huawei_gexport_cdma')
    op.drop_table('APINFO_CG', schema='huawei_gexport_cdma')
    op.drop_table('APPCERT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('ATMOAMCFG_USN', schema='huawei_gexport_cdma')
    op.drop_table('BBUFAN_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('BFDSESSION_USN', schema='huawei_gexport_cdma')
    op.drop_table('BFD_USN', schema='huawei_gexport_cdma')
    op.drop_table('BINDGTPCIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('BINDGTPUIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('BINDINGCON_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('BINDINGRULE_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('BOARD_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('BRDIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('BRD_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('BSSAPPTMR_USN', schema='huawei_gexport_cdma')
    op.drop_table('BSSGP_USN', schema='huawei_gexport_cdma')
    op.drop_table('BWRATIO_USN', schema='huawei_gexport_cdma')
    op.drop_table('CABINET_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CAMELSPT_USN', schema='huawei_gexport_cdma')
    op.drop_table('CAMELTMR_USN', schema='huawei_gexport_cdma')
    op.drop_table('CASCADEPORT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CCHARACTER_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('CDRBACKUP_CG', schema='huawei_gexport_cdma')
    op.drop_table('CDRDISTR_CG', schema='huawei_gexport_cdma')
    op.drop_table('CDRPROC_CG', schema='huawei_gexport_cdma')
    op.drop_table('CDRROUTE_CG', schema='huawei_gexport_cdma')
    op.drop_table('CDRSTOR_CG', schema='huawei_gexport_cdma')
    op.drop_table('CDRSYNC_CG', schema='huawei_gexport_cdma')
    op.drop_table('CELL_USN', schema='huawei_gexport_cdma')
    op.drop_table('CERTCFG_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CERTCHKTSK_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CERTDEPLOY_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CERTMK_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CERTREQ_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CGEquipment_CG', schema='huawei_gexport_cdma')
    op.drop_table('CGFunction_CG', schema='huawei_gexport_cdma')
    op.drop_table('CGMG_CG', schema='huawei_gexport_cdma')
    op.drop_table('CGMODULE_CG', schema='huawei_gexport_cdma')
    op.drop_table('CGPOMUEquipment_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('CGPOMUFunction_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('CGSYSRES_CG', schema='huawei_gexport_cdma')
    op.drop_table('CHGCDPIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('CHGCDR_USN', schema='huawei_gexport_cdma')
    op.drop_table('CHGCG_USN', schema='huawei_gexport_cdma')
    op.drop_table('CHGCHAR_USN', schema='huawei_gexport_cdma')
    op.drop_table('CHGGA_USN', schema='huawei_gexport_cdma')
    op.drop_table('CHGPLMNCHAR_USN', schema='huawei_gexport_cdma')
    op.drop_table('CHGWKDY_USN', schema='huawei_gexport_cdma')
    op.drop_table('CHK_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CHRCFG_USN', schema='huawei_gexport_cdma')
    op.drop_table('COMPATIBILITY_USN', schema='huawei_gexport_cdma')
    op.drop_table('CONNECTPLMN_USN', schema='huawei_gexport_cdma')
    op.drop_table('CORE_USN', schema='huawei_gexport_cdma')
    op.drop_table('CPUDR_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('CRLPOLICY_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('DEVADDR_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('DEVIP_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('DFTRT_USN', schema='huawei_gexport_cdma')
    op.drop_table('DHCPRELAYSWITCH_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('DHCPSW_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('DIAMPEERPP_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('DIAMPP_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('DIFPRI_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('DMFUNC_USN', schema='huawei_gexport_cdma')
    op.drop_table('DMLE_USN', schema='huawei_gexport_cdma')
    op.drop_table('DMLKS_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('DMLKS_USN', schema='huawei_gexport_cdma')
    op.drop_table('DMLNKEX_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('DMLNK_USN', schema='huawei_gexport_cdma')
    op.drop_table('DMPEEREX_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('DMPE_USN', schema='huawei_gexport_cdma')
    op.drop_table('DMRT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('DMRT_USN', schema='huawei_gexport_cdma')
    op.drop_table('DNSCLTIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('DNSS_USN', schema='huawei_gexport_cdma')
    op.drop_table('DNS_USN', schema='huawei_gexport_cdma')
    op.drop_table('DRACAPACITY_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('DSCPMAP_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('DSCPQOS_USN', schema='huawei_gexport_cdma')
    op.drop_table('DSCPRMK_USN', schema='huawei_gexport_cdma')
    op.drop_table('DSGNETYPE_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('DSGNETYPE_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('EDRREPORT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('EMM_USN', schema='huawei_gexport_cdma')
    op.drop_table('EMSTZ_CG', schema='huawei_gexport_cdma')
    op.drop_table('EMSTZ_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('EMSTZ_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('EMSTZ_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('EMSTZ_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('EMSTZ_USN', schema='huawei_gexport_cdma')
    op.drop_table('EMSTZ_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('EQUIPMENT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('ESM_USN', schema='huawei_gexport_cdma')
    op.drop_table('ETHPORT_USN', schema='huawei_gexport_cdma')
    op.drop_table('ETHPORT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('FCRULE_PRIORITY_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('FCSRVANA_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('FCSRVFILT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('FENUMTYPE_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('FEPLUG_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('FLOWCTRLBUF_USN', schema='huawei_gexport_cdma')
    op.drop_table('FLOWCTRL_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('FLOWCTRL_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('FTPCLT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('GBACCAREALST_USN', schema='huawei_gexport_cdma')
    op.drop_table('GBARD_USN', schema='huawei_gexport_cdma')
    op.drop_table('GBAUTHCIPH_USN', schema='huawei_gexport_cdma')
    op.drop_table('GBDETACH_USN', schema='huawei_gexport_cdma')
    op.drop_table('GBIPLOCENDPT_USN', schema='huawei_gexport_cdma')
    op.drop_table('GBPAGING_USN', schema='huawei_gexport_cdma')
    op.drop_table('GBSM_USN', schema='huawei_gexport_cdma')
    op.drop_table('GGSNCHARACT_USN', schema='huawei_gexport_cdma')
    op.drop_table('GMM_USN', schema='huawei_gexport_cdma')
    op.drop_table('GPS_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('GTPPUB_USN', schema='huawei_gexport_cdma')
    op.drop_table('GTPUCTRL_USN', schema='huawei_gexport_cdma')
    op.drop_table('GTRANSPARAGW_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('GTRANSPARA_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('HPLMN_USN', schema='huawei_gexport_cdma')
    op.drop_table('IFIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('IKECFG_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('IMSIGT_USN', schema='huawei_gexport_cdma')
    op.drop_table('IMSIHSS_USN', schema='huawei_gexport_cdma')
    op.drop_table('IMSISMCHAR_USN', schema='huawei_gexport_cdma')
    op.drop_table('INAP_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('INGCHKTSK_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('INSP_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('INSP_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('INTERCONNE_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_CG', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_UGW', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_USN', schema='huawei_gexport_cdma')
    op.drop_table('InventoryBoard_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_CG', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_UGW', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_USN', schema='huawei_gexport_cdma')
    op.drop_table('InventoryFrame_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVerOutSource_CG', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_CG', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_UGW', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_USN', schema='huawei_gexport_cdma')
    op.drop_table('InventoryHostVer_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('InventoryPort_UGW', schema='huawei_gexport_cdma')
    op.drop_table('InventoryPort_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_CG', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_UGW', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_USN', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_CG', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_UGW', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_USN', schema='huawei_gexport_cdma')
    op.drop_table('InventorySlot_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('IPADDR_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('IPADDR_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('IPCBASEIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('IPGUARD_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('IPNM_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('IPNSVC_USN', schema='huawei_gexport_cdma')
    op.drop_table('IPPAIR_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('IPPORT_EXTEND_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('IPPORT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('IPQOS_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('IPRESOURCE_CG', schema='huawei_gexport_cdma')
    op.drop_table('IPRT_USN', schema='huawei_gexport_cdma')
    op.drop_table('IPRT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('IPSECCFG_USN', schema='huawei_gexport_cdma')
    op.drop_table('IPV4DNSH_USN', schema='huawei_gexport_cdma')
    op.drop_table('IPVLANPRI_USN', schema='huawei_gexport_cdma')
    op.drop_table('IUACCAREALST_USN', schema='huawei_gexport_cdma')
    op.drop_table('IUARD_USN', schema='huawei_gexport_cdma')
    op.drop_table('IUAUTHCIPH_USN', schema='huawei_gexport_cdma')
    op.drop_table('IUDETACH_USN', schema='huawei_gexport_cdma')
    op.drop_table('IULOAD_USN', schema='huawei_gexport_cdma')
    op.drop_table('IUPAGING_USN', schema='huawei_gexport_cdma')
    op.drop_table('IUSM_USN', schema='huawei_gexport_cdma')
    op.drop_table('LAIVLR_USN', schema='huawei_gexport_cdma')
    op.drop_table('LDSMR_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('LICCTRL_USN', schema='huawei_gexport_cdma')
    op.drop_table('LICENSEINFO_USN', schema='huawei_gexport_cdma')
    op.drop_table('LICRATE_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('LINKTYPE_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('LLDPGLOBAL_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('LN_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('LOCALETHPORT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('LOCALIP_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('LOCALNRI_USN', schema='huawei_gexport_cdma')
    op.drop_table('LOCALPARA_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('LOCATION_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('M3DE_USN', schema='huawei_gexport_cdma')
    op.drop_table('M3LE_USN', schema='huawei_gexport_cdma')
    op.drop_table('M3LKS_USN', schema='huawei_gexport_cdma')
    op.drop_table('M3LNK_USN', schema='huawei_gexport_cdma')
    op.drop_table('M3RT_USN', schema='huawei_gexport_cdma')
    op.drop_table('MANRESALMRPT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('MAPFUNC_USN', schema='huawei_gexport_cdma')
    op.drop_table('MBMSBRRES_USN', schema='huawei_gexport_cdma')
    op.drop_table('MEPROCESS_USN', schema='huawei_gexport_cdma')
    op.drop_table('ME_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('MMEID_USN', schema='huawei_gexport_cdma')
    op.drop_table('MMFUNC_USN', schema='huawei_gexport_cdma')
    op.drop_table('MODULE_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('MTP3BTMR_USN', schema='huawei_gexport_cdma')
    op.drop_table('MTP3TMR_USN', schema='huawei_gexport_cdma')
    op.drop_table('MVNOFUN_USN', schema='huawei_gexport_cdma')
    op.drop_table('MVNONET_USN', schema='huawei_gexport_cdma')
    op.drop_table('MVNORES_USN', schema='huawei_gexport_cdma')
    op.drop_table('MVNO_USN', schema='huawei_gexport_cdma')
    op.drop_table('N7ALMT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('NEMNT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('NE_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('NODE_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('NOTIFYCFG_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('NSE_USN', schema='huawei_gexport_cdma')
    op.drop_table('NS_USN', schema='huawei_gexport_cdma')
    op.drop_table('NTPCLIENTIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('NTPCP_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('OFFLOADINF_USN', schema='huawei_gexport_cdma')
    op.drop_table('OMCH_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('OPC_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('OP_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('OSPF_USN', schema='huawei_gexport_cdma')
    op.drop_table('PAGINGRULE4STAT_USN', schema='huawei_gexport_cdma')
    op.drop_table('PAIREDBOARDS_USN', schema='huawei_gexport_cdma')
    op.drop_table('PCEFABIDICT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PCEFABIITEM_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PDHOSTCFG_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PDPAPN_USN', schema='huawei_gexport_cdma')
    op.drop_table('PDPCAR_USN', schema='huawei_gexport_cdma')
    op.drop_table('PDREALMCFG_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PDU_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('PEERL_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PEERPLMN_USN', schema='huawei_gexport_cdma')
    op.drop_table('PERFAPN_USN', schema='huawei_gexport_cdma')
    op.drop_table('PEU_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('PFBW_USN', schema='huawei_gexport_cdma')
    op.drop_table('PFRES_USN', schema='huawei_gexport_cdma')
    op.drop_table('PGWFLOWCTRL_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('PHYPORT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('PMGRPORT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PMM_USN', schema='huawei_gexport_cdma')
    op.drop_table('PMSCFG_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PMSNTFCFG_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('POOLNRI_USN', schema='huawei_gexport_cdma')
    op.drop_table('POOL_USN', schema='huawei_gexport_cdma')
    op.drop_table('PORTIPPOOL_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('PORTPOLICY_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('PORT_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('PORT_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('PPCEFCAT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PRBLIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('PRBPEER_USN', schema='huawei_gexport_cdma')
    op.drop_table('PRBSW_USN', schema='huawei_gexport_cdma')
    op.drop_table('PREALMRT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PRI2QUE_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('PROCESSGRP_USN', schema='huawei_gexport_cdma')
    op.drop_table('PSRVCFG_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('PUBLICAPNNI_USN', schema='huawei_gexport_cdma')
    op.drop_table('PUBNWIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('PWDPOLICY_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('QOSDSCP_USN', schema='huawei_gexport_cdma')
    op.drop_table('RACK_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('RADIUSPP_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('RAID_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('RESOURCE_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('RIPTIMER_USN', schema='huawei_gexport_cdma')
    op.drop_table('RIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('RLOCATION_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('RNC_USN', schema='huawei_gexport_cdma')
    op.drop_table('RTDHOST_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('RTENT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('RTEXIT_SMNM_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('RTEXIT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('RTRESULT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('S1ACCAREALST_USN', schema='huawei_gexport_cdma')
    op.drop_table('S1APLE_USN', schema='huawei_gexport_cdma')
    op.drop_table('S1APPARA_USN', schema='huawei_gexport_cdma')
    op.drop_table('S1ARD_USN', schema='huawei_gexport_cdma')
    op.drop_table('S1USRSECPARA_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCANPARA_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('SCANSW_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('SCCPDPC_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCCPEXT_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SCCPGT_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCCPOPC_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCCPSSN_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCCPTMR_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCTPASPEERADDR_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCTPCFG_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SCTPPARA_USN', schema='huawei_gexport_cdma')
    op.drop_table('SCTPPP_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SDBTMR_USN', schema='huawei_gexport_cdma')
    op.drop_table('SEQCHK_USN', schema='huawei_gexport_cdma')
    op.drop_table('SFP_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('SGSNCHARACT_USN', schema='huawei_gexport_cdma')
    op.drop_table('SIGATTR_USN', schema='huawei_gexport_cdma')
    op.drop_table('SLOT_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('SMFUNC_USN', schema='huawei_gexport_cdma')
    op.drop_table('SMS_USN', schema='huawei_gexport_cdma')
    op.drop_table('SNDCP_USN', schema='huawei_gexport_cdma')
    op.drop_table('SOAPPP_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('SPSV3DA_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SPSV3DMLNK_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SPSV3DMPEER_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SPSV3FCRULE_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SPSV3MODULE_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SPSV3TimeZone_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('SSL_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('STCFLOWCTRL_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('SUBDATA_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('SUBIF_USN', schema='huawei_gexport_cdma')
    op.drop_table('SUBRACK_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('SUBRACK_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('SYSCAP_USN', schema='huawei_gexport_cdma')
    op.drop_table('SYSINFO_USN', schema='huawei_gexport_cdma')
    op.drop_table('SYS_USN', schema='huawei_gexport_cdma')
    op.drop_table('TAIGROUP_USN', schema='huawei_gexport_cdma')
    op.drop_table('TAILAI_USN', schema='huawei_gexport_cdma')
    op.drop_table('TAI_USN', schema='huawei_gexport_cdma')
    op.drop_table('TAKEOVER_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('TALST_USN', schema='huawei_gexport_cdma')
    op.drop_table('TASM_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('TDFROUTE_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('TIMER_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('TIMESRC_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('TIMESTRFMT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('TIMETHRD_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('TLFRSWITCH_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('TRUSTCERT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('TZ_UGW', schema='huawei_gexport_cdma')
    op.drop_table('TZ_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('UEFU_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('UETYPE_USN', schema='huawei_gexport_cdma')
    op.drop_table('UGTP_USN', schema='huawei_gexport_cdma')
    op.drop_table('UGWAPNPGW_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWAPN_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWBoard_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWCG_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWCPU_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWDRA_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWEPSNSCTPASSOC_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWEPSNSPUINSTANCE_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWEquipment_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWFrame_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWFunction_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWHPLMN_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWIpAddrTable_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWIpRouteTable_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWIpTransTable_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWNORTH_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWOCS_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPCRFHOST_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPCRF_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPGWFUNCTION_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPHGWDOMAIN_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPHGWPOOL_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPHYPORTPGW_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPHYPORTSGW_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPHYPORT_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPoolPGW_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPool_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWPRODUCTTYPE_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWRADIUSAAA_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWSCTPASSOC_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWSERVICEINSTANCE_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWSGWFUNCTION_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWSPUINSTANCE_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWTGWAPN_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWTGWDOMAIN_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWTGWSPUINSTANCE_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWTUNNEL_UGW', schema='huawei_gexport_cdma')
    op.drop_table('UGWVER_UGW', schema='huawei_gexport_cdma')
    op.drop_table('ULPU_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('UPCCBOARD_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCEquipment_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCETHPORT_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCFunction_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCIPADDR_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCLOCATION_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCMODULEEX_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCMODULE_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCPCRF_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCPDIAML_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCPDIAMP_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCPEER_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCPMSLINKCFG_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCRDSG_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCRIPADDR_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCRLOCATION_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('UPCCSCTPASSOC_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('USB_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('USCDBCLUSTER_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBDSGSCTPPARA_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBEquipment_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBETHPORT_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBFunction_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBIPADDR_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBMODULE_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBNODE_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBNORTHFUNC_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBPROVSTATOBJ_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBRDSG_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBRIPADDR_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBRLOCATION_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBSCTPASSOC_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBSTRNG_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USCDBSUBSCRIBER_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('USN2GPAGING_USN', schema='huawei_gexport_cdma')
    op.drop_table('USN3GPAGING_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNBFDSESSION_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNBSSID_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNCG_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNDNSServer_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNEquipment_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNFunction_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNIFIP_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNIMSIGT_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNIPNSVC_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNIPRoute_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNLicense_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNM3UADE_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNM3UALE_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNM3UALinkSet_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNM3UALink_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNMVNO_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNRNCInfo_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNSCCPOPC_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNSCCPSignallingPoint_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNSCCPSSN_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNSIGATTR_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNSYSCAP_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNSYSInfo_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNSYS_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNVLAN_USN', schema='huawei_gexport_cdma')
    op.drop_table('USNVLR_USN', schema='huawei_gexport_cdma')
    op.drop_table('USRATTR_USN', schema='huawei_gexport_cdma')
    op.drop_table('USRPDPCAP_USN', schema='huawei_gexport_cdma')
    op.drop_table('VLANMAP_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('VLANPORT_USN', schema='huawei_gexport_cdma')
    op.drop_table('VLAN_USN', schema='huawei_gexport_cdma')
    op.drop_table('VLR_USN', schema='huawei_gexport_cdma')
    op.drop_table('VRF_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('WEBLMT_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('WRED_USN', schema='huawei_gexport_cdma')