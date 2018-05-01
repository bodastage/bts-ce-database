"""Create Huawei LTE tables for GExport format

Revision ID: 74e93b490a26
Revises: 997b8aa5acfa
Create Date: 2018-04-12 11:51:00.638000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74e93b490a26'
down_revision = '997b8aa5acfa'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('eNodeBCell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AdditionalSpectrumEmission', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AirCellFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CPRICompression', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellActiveState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellAdminState', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellRadius', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellRadiusStartLocation', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellScaleInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellSpecificOffset', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CnOpSharingGroupId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CrsPortNum', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CsgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CustomizedBandWidthCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DlBandWidth', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DlCyclicPrefix', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DlEarfcn', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EmergencyAreaIdCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('EuCellStandbyMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FddTddInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FreqBand', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('FreqPriorityForAnr', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HighSpeedFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IntraFreqAnrInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('IntraFreqRanSharingInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MultiCellShareMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MultiRruCellFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NbCellFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PhyCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PreambleFmt', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('QoffsetFreq', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RootSequenceIdx', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SpecifiedCellFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TxRxMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UePowerMaxCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UlBandWidth', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UlCyclicPrefix', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UlEarfcnCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('WorkMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )


    op.create_table('eNodeBUtranNCell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RncId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AnrFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BlindHoPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellMeasPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CtrlMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NCellMeasPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoHoFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoRmvFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OverlapInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBEUtranIntraFreqNCell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('eNodeBId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AnrFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AttachCellSwitch', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellIndividualOffset', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellMeasPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellQoffset', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellRangeExpansion', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CtrlMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HighSpeedCellIndOffset', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NCellClassLabel', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoHoFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoRmvFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VectorCellFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBEUtranInterFreqNCell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('eNodeBId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AggregationProperty', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AnrFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BlindHoPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellIndividualOffset', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellMeasPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellQoffset', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CtrlMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NCellClassLabel', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoHoFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoRmvFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OverlapInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OverlapIndicatorExtension', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OverlapRange', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBGeranNcell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GeranCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Lac', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AnrFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BlindHoPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CtrlMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NCellMeasPriority', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NeighbourCellName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoHoFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NoRmvFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OverlapInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBEUtranExternalCell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('eNodeBId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AnrFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CtrlMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DlEarfcn', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DlFreqOffset', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('HighSpeedFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NbCellFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NclUpdateMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PhyCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RoamingAreaHoInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SpecifiedCellFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SupportEmtcFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Tac', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UlEarfcnCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBEutranExternalCellPlmn_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ShareMcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ShareMnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('eNodeBId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBGeranExternalCell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GeranCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Lac', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AnrFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BandIndicator', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('BaseStationColourCode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CsPsHOInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CtrlMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DtmInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('GeranArfcn', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NetworkColourCode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RacCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RoamingAreaHoInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UltraFlashCsfbInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBUtranExternalCell_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RncId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UtranCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('AnrFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CsPsHOInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CtrlMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Lac', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PScrambCode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Rac', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RacCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RoamingAreaHoInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UtranDlArfcn', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UtranFddTddType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('UtranUlArfcnCfgInd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBUtranExternalCellPlmn_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RncId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ShareMcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ShareMnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('NE_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CLOUDBBID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('INTERFACEID', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LMTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LOCATION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NERMVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PRODUCTVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('SWVERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeB_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('eNodeBId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBCNOPERATOR_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CnOperatorId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CnOperatorName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CnOperatorType', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mcc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Mnc', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OperatorFunSwitch', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('PlmnMode', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBCellOp_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('LocalCellId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TrackingAreaId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CellReservedForOp', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('MMECfgNum', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpDlRbUsedRatio', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpNonGbrResourceRatio', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpPttDlRbHighThd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpPttDlRbLowThd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpPttUlRbHighThd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpPttUlRbLowThd', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpResourceGroupIndex', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpUeNumRatio', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OpUlRbUsedRatio', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('OperatorPlmnRoundPeriod', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('RatFreqPriorityGroupId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

    op.create_table('eNodeBCnOperatorTa_eNodeB',
        sa.Column('FILENAME', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('DATETIME', sa.DateTime, autoincrement=False, nullable=True),
        sa.Column('TECHNOLOGY', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VENDOR', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('VERSION', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NETYPE', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('TrackingAreaId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('CnOperatorId', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('ENodeBFunctionName', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('NbIotTaFlag', sa.CHAR(length=250), autoincrement=False, nullable=True),
        sa.Column('Tac', sa.CHAR(length=250), autoincrement=False, nullable=True),
        schema='huawei_gexport_lte'
    )

def downgrade():
    op.drop_table('eNodeBCell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBEUtranIntraFreqNCell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBUtranNCell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBEUtranInterFreqNCell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBGeranNcell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBEUtranExternalCell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBEutranExternalCellPlmn_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBGeranExternalCell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBUtranExternalCell_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBUtranExternalCellPlmn_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('NE_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeB_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBCNOPERATOR_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBCellOp_eNodeB', schema='huawei_gexport_lte')
    op.drop_table('eNodeBCnOperatorTa_eNodeB', schema='huawei_gexport_lte')
