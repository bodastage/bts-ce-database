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
                    sa.Column('PN', sa.CHAR(length=250), autoincrement=False, nullable=True),
                    sa.Column('REFERABLE', sa.CHAR(length=250), autoincrement=False, nullable=True),
                    sa.Column('RN', sa.CHAR(length=250), autoincrement=False, nullable=True),
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

    op.create_table('CGPOMUFunction_CGPOMU',
                    sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
                    sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
                    sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
                    sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
                    sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
                    sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
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


def downgrade():
    op.drop_table('CELL_USN', schema='huawei_gexport_cdma')
    op.drop_table('CDRROUTE_CG', schema='huawei_gexport_cdma')
    op.drop_table('CORE_USN', schema='huawei_gexport_cdma')
    op.drop_table('BINDINGCON_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('BOARD_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('BRD_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('CABINET_USU3910', schema='huawei_gexport_cdma')
    op.drop_table('CCHARACTER_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('CGPOMUFunction_CGPOMU', schema='huawei_gexport_cdma')
    op.drop_table('DEVADDR_UPCC', schema='huawei_gexport_cdma')
    op.drop_table('DIAMPEERPP_SPSV3', schema='huawei_gexport_cdma')
    op.drop_table('FLOWCTRL_USCDB', schema='huawei_gexport_cdma')
    op.drop_table('InventoryRack_UGW', schema='huawei_gexport_cdma')
