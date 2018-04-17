"""Add migrations for Huawei WCDMA BSC6900

Revision ID: b2031f71d167
Revises: bcf65a006663
Create Date: 2018-04-11 10:40:15.136000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2031f71d167'
down_revision = 'bcf65a006663'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('UCELL_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACTSTATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BANDIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BLKSTATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CCHCNOPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLCOVERAGETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLHETFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CFGRACIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CIO', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNOPGRPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DISPLAYPERFDATADEACELL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DLPOWERAVERAGEWINDOWSIZE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DLTPCPATTERN01COUNT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DPGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSSFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSSSMALLCOVMAXTXPOWER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ERACHACTFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FLEXUEGROUPNETLAYERID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOSTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IPDLFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCELL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MAXTXPOWER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MBMSACTFLG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MIMOACTFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NEEDSELFPLANFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NINSYNCIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODESYNSWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NOUTSYNCIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('POWERRAISELIMIT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRIORITY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSCRAMBCODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('REMARK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPGID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SPLITCELLIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SRN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SSN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPBMC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TCELL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TIMER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRLFAILURE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TXDIVERSITYIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UARFCNDOWNLINK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UARFCNUPLINK', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UARFCNUPLINKIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VPLIMITIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('SYS_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SUPPORTRNCINPOOL', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSCONTACT', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSDESC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSLOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSOBJECTID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SYSSERVICES', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('NodeBFunction',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('APPLICATIONREF', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTERFACEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LMTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NERMVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBFUNCTIONNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OBJID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRODUCTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('PICH_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PHYCHID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PICHID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PICHMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('STTDIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('BCH_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BCHPOWER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRCHID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('PSCH_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CELLID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PHYCHID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PSCHPOWER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('CNOPERATOR_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNOPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNOPERATORNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MCC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MNC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OPERATORTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('URA_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNOPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('URAID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('LAC_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNOPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LAC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLMNVALTAGMAX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PLMNVALTAGMIN', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('NODEB_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ACTSTATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AUTOHOMINGFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BLKSTATUS', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CNOPINDEX', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DSSFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HOSTTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IDTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IUBFLEXFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBAUTOREDUNDANCYFLAG', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBNAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBPROTCLVER', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBTRACESWITCH', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSCMNGMODE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SATELLITEIND', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SHARINGTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SIGNALCREATETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TNLBEARERTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TRANSDELAY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )

    op.create_table('NODEBALGOPARA_BSC6900UMTS',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOGICRNCID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ADPETADJFUNCSW', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HSUPACECONSUMESELECTION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IDTYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IUBBWCGSTTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IUBBWNONCGSTTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IUBREMAINBWTHD', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NBMINNERSWITCH_CELL_BASIC_CCH_DL_CE_CAC', sa.CHAR(length=250), autoincrement=False,
                  nullable=True),
        sa.Column('NBMINNERSWITCH_CELL_BASIC_CCH_UL_CE_CAC', sa.CHAR(length=250), autoincrement=False,
                  nullable=True),
        sa.Column('NODEBALGOENHSWITCH_ENH_DYNCAPSFC_ON_NCP', sa.CHAR(length=250), autoincrement=False,
                  nullable=True),
        sa.Column('NODEBALGOENHSWITCH_NODEB_CRYSTAL_VOICE_DEEPCOVER_SWITCH', sa.CHAR(length=250),
                  autoincrement=False, nullable=True),
        sa.Column('NODEBALGOENHSWITCH_NODEB_IMPVD_UL_COVER_FOR_SRBODCH_SWITCH', sa.CHAR(length=250),
                  autoincrement=False, nullable=True),
        sa.Column('NODEBALGOENHSWITCH_NODEB_SEAMLESS_CRYSTAL_VOICE_SWITCH', sa.CHAR(length=250),
                  autoincrement=False, nullable=True),
        sa.Column('NODEBHSDPAMAXUSERNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBHSUPAMAXUSERNUM', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBLDCALGOSWITCH_IUB_LDR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBLDCALGOSWITCH_IUB_OLC', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NODEBLDCALGOSWITCH_LCG_CREDIT_CLB_SWITCH', sa.CHAR(length=250), autoincrement=False,
                  nullable=True),
        sa.Column('NODEBLDCALGOSWITCH_LCG_CREDIT_LDR', sa.CHAR(length=250), autoincrement=False,
                  nullable=True),
        sa.Column('NODEBLDCALGOSWITCH_NODEB_CREDIT_CLB_SWITCH', sa.CHAR(length=250), autoincrement=False,
                  nullable=True),
        sa.Column('NODEBLDCALGOSWITCH_NODEB_CREDIT_LDR', sa.CHAR(length=250), autoincrement=False,
                  nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT1', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT10', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT11', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT12', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT13', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT14', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT15', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT16', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT4', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT5', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT6', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT7', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT8', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA1_RSVDBIT9', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA2', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVDPARA3', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RSVSWITCH0', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UPLINKACTIVESETEXP_CCPIC_PHASE2_COORDINATING_RL_SWITCH', sa.CHAR(length=250),
                  autoincrement=False, nullable=True),
        sa.Column('UPLINKACTIVESETEXP_IMPRV_ULCOV_SRBOD_COORDINATING_RL_SWITCH', sa.CHAR(length=250),
                  autoincrement=False, nullable=True),
        sa.Column('UPLINKACTIVESETEXP_SMLESSCRSTVOICE_COORDINATING_RL_SWITCH', sa.CHAR(length=250),
                  autoincrement=False, nullable=True),
        schema='huawei_gexport_wcdma'
        )


def downgrade():
    op.drop_table('UCELL_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('SYS_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('NodeBFunction', schema='huawei_gexport_wcdma')
    op.drop_table('PICH_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('BCH_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('PSCH_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('CNOPERATOR_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('URA_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('LAC_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('NODEB_BSC6900UMTS', schema='huawei_gexport_wcdma')
    op.drop_table('NODEBALGOPARA_BSC6900UMTS', schema='huawei_gexport_wcdma')
