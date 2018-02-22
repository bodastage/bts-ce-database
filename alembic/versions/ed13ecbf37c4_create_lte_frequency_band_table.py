"""Create LTE Frequency band table

Revision ID: ed13ecbf37c4
Revises: eab3475f6f35
Create Date: 2018-02-22 02:34:46.730000

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'ed13ecbf37c4'
down_revision = 'eab3475f6f35'
branch_labels = None
depends_on = None


def upgrade():
    """
    Frequencies and Bandwidths are in MHz

    LTE frequency band 36.101 (Rel 15 Dec 2017)

    F_dl = F_dl_low + 0.1 (N_dl-N_dl_low)
    F_ul = F_ul_low + 0.1(N_ul-N_ul_low)

    F_dl - Downlink Frequency
    F_dl_low = Lowest DL Frequency for band
    N_dl - Downlink EUARFCN
    N_dl_low - Lowest Downlink EUARFCN

    """
    op.create_table(
        'lte_frequency_bands',
        sa.Column('pk', sa.Integer, primary_key=True,  nullable=False),
        sa.Column('band_id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('dl_freq_low', sa.Float),
        sa.Column('dl_freq_middle', sa.Float),
        sa.Column('dl_freq_high', sa.Float),
        sa.Column('dl_arfcn_low', sa.Float),
        sa.Column('dl_arfcn_middle', sa.Float),
        sa.Column('dl_arfcn_high', sa.Float),
        sa.Column('dl_bandwidth', sa.Float),
        sa.Column('ul_bandwidth', sa.Float),
        sa.Column('ul_freq_low', sa.Float),
        sa.Column('ul_freq_middle', sa.Float),
        sa.Column('ul_freq_high', sa.Float),
        sa.Column('ul_arfcn_low', sa.Float),
        sa.Column('ul_arfcn_middle', sa.Float),
        sa.Column('ul_arfcn_high', sa.Float),
        sa.Column('duplex_spacing', sa.Float),
        sa.Column('geographical_area', sa.String(100)),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )
    op.execute('ALTER SEQUENCE  lte_frequency_bands_pk_seq RENAME TO seq_lte_frequency_bands_pk')

    lte_frequency_bands = sa.sql.table(
        'lte_frequency_bands',
        sa.Column('pk', sa.Integer, sa.Sequence('seq_lte_frequency_bands_pk', ), primary_key=True, nullable=False),
        sa.Column('band_id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('dl_freq_low', sa.Float),
        sa.Column('dl_freq_middle', sa.Float),
        sa.Column('dl_freq_high', sa.Float),
        sa.Column('dl_arfcn_low', sa.Float),
        sa.Column('dl_arfcn_middle', sa.Float),
        sa.Column('dl_arfcn_high', sa.Float),
        sa.Column('dl_bandwidth', sa.Float),
        sa.Column('ul_bandwidth', sa.Float),
        sa.Column('ul_freq_low', sa.Float),
        sa.Column('ul_freq_middle', sa.Float),
        sa.Column('ul_freq_high', sa.Float),
        sa.Column('ul_arfcn_low', sa.Float),
        sa.Column('ul_arfcn_middle', sa.Float),
        sa.Column('ul_arfcn_high', sa.Float),
        sa.Column('duplex_spacing', sa.Float),
        sa.Column('geographical_area', sa.String(100)),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow)
    )

    op.bulk_insert(lte_frequency_bands, [
        {'band_id': 1, 'name': '2100',
         'dl_freq_low': 2110, 'dl_freq_middle':2140, 'dl_freq_high': 2170,
         'dl_arfcn_low': 0,'dl_arfcn_middle':300,  'dl_arfcn_high':599,
         'dl_bandwidth': 60, 'ul_bandwidth': 60,
         'ul_freq_low':1920, 'ul_freq_middle':1950,  'ul_freq_high':1980,
         'ul_arfcn_low':18000, 'ul_arfcn_middle':18300,'ul_arfcn_high':18599,
         'duplex_spacing':190, 'geographical_area': 'Global',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 2, 'name': '1900 PCS',
         'dl_freq_low': 1930, 'dl_freq_middle': 1960, 'dl_freq_high': 1990,
         'dl_arfcn_low': 600, 'dl_arfcn_middle': 900, 'dl_arfcn_high': 1199,
         'dl_bandwidth': 60, 'ul_bandwidth': 60,
         'ul_freq_low': 1850, 'ul_freq_middle': 1880, 'ul_freq_high': 1910,
         'ul_arfcn_low': 18600, 'ul_arfcn_middle': 18900, 'ul_arfcn_high': 19199,
         'duplex_spacing': 80, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 3, 'name': '1800+',
         'dl_freq_low': 1805, 'dl_freq_middle': 1842.5, 'dl_freq_high': 1880,
         'dl_arfcn_low': 1200, 'dl_arfcn_middle': 1575, 'dl_arfcn_high': 1949,
         'dl_bandwidth': 75, 'ul_bandwidth': 75,
         'ul_freq_low': 1710, 'ul_freq_middle': 1747.5, 'ul_freq_high': 1785,
         'ul_arfcn_low': 19200, 'ul_arfcn_middle': 19575, 'ul_arfcn_high': 19949,
         'duplex_spacing': 95,'geographical_area': 'Global',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 4, 'name': 'AWS-1',
         'dl_freq_low': 2110, 'dl_freq_middle': 2132.5, 'dl_freq_high': 2155,
         'dl_arfcn_low': 1950, 'dl_arfcn_middle': 2175, 'dl_arfcn_high': 2399,
         'dl_bandwidth': 45, 'ul_bandwidth': 45,
         'ul_freq_low': 1710, 'ul_freq_middle': 1732.5, 'ul_freq_high': 1755,
         'ul_arfcn_low': 19950, 'ul_arfcn_middle': 20175, 'ul_arfcn_high': 20399,
         'duplex_spacing': 400, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 5, 'name': '850',
         'dl_freq_low': 869, 'dl_freq_middle':881.5 , 'dl_freq_high': 894,
         'dl_arfcn_low': 2400, 'dl_arfcn_middle': 2525, 'dl_arfcn_high': 2649,
         'dl_bandwidth': 25, 'ul_bandwidth': 25,
         'ul_freq_low': 824, 'ul_freq_middle': 836.5, 'ul_freq_high': 849,
         'ul_arfcn_low': 20400, 'ul_arfcn_middle': 20525, 'ul_arfcn_high': 20649,
         'duplex_spacing': 45, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 6, 'name': 'UMTS only',
         'dl_freq_low': 875, 'dl_freq_middle': 880, 'dl_freq_high': 885,
         'dl_arfcn_low': 2650, 'dl_arfcn_middle': 2700, 'dl_arfcn_high': 2749,
         'dl_bandwidth': 10, 'ul_bandwidth': 10,
         'ul_freq_low': 830, 'ul_freq_middle': 835, 'ul_freq_high': 840,
         'ul_arfcn_low': 20650, 'ul_arfcn_middle': 20700, 'ul_arfcn_high': 20749,
         'duplex_spacing': 45, 'geographical_area': 'APAC',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 7, 'name': '2600',
         'dl_freq_low': 2620, 'dl_freq_middle': 2655, 'dl_freq_high': 2690,
         'dl_arfcn_low': 2750, 'dl_arfcn_middle': 3100, 'dl_arfcn_high': 3449,
         'dl_bandwidth': 70, 'ul_bandwidth': 70,
         'ul_freq_low': 2500, 'ul_freq_middle': 2535, 'ul_freq_high': 2570,
         'ul_arfcn_low': 20750, 'ul_arfcn_middle': 21100, 'ul_arfcn_high': 21449,
         'duplex_spacing': 120, 'geographical_area': 'EMEA',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 8, 'name': '900 GSM',
         'dl_freq_low': 925, 'dl_freq_middle': 942.5, 'dl_freq_high': 960,
         'dl_arfcn_low': 3450, 'dl_arfcn_middle': 3625, 'dl_arfcn_high': 3799,
         'dl_bandwidth': 35, 'ul_bandwidth': 35,
         'ul_freq_low': 880, 'ul_freq_middle': 897.5, 'ul_freq_high': 915,
         'ul_arfcn_low': 21450, 'ul_arfcn_middle': 21625, 'ul_arfcn_high': 21799,
         'duplex_spacing': 45, 'geographical_area': 'Global',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 9, 'name': '1800',
         'dl_freq_low': 1844.9, 'dl_freq_middle': 1862.4, 'dl_freq_high': 1879.9,
         'dl_arfcn_low': 3800, 'dl_arfcn_middle': 3975, 'dl_arfcn_high': 4149,
         'dl_bandwidth': 35, 'ul_bandwidth': 35,
         'ul_freq_low': 1749.9, 'ul_freq_middle': 1767.4, 'ul_freq_high': 1784.9,
         'ul_arfcn_low': 21800, 'ul_arfcn_middle': 21975, 'ul_arfcn_high': 22149,
         'duplex_spacing': 95, 'geographical_area': 'APAC',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 10, 'name': 'AWS-1+',
         'dl_freq_low': 2110, 'dl_freq_middle': 2140, 'dl_freq_high': 2170,
         'dl_arfcn_low': 4150, 'dl_arfcn_middle': 4450, 'dl_arfcn_high': 4749,
         'dl_bandwidth': 60, 'ul_bandwidth': 60,
         'ul_freq_low': 1710, 'ul_freq_middle': 1740, 'ul_freq_high': 1770,
         'ul_arfcn_low': 22150, 'ul_arfcn_middle': 22450, 'ul_arfcn_high': 22749,
         'duplex_spacing': 400, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 11, 'name': '1500 Lower',
         'dl_freq_low': 1475.9, 'dl_freq_middle': 1485.9, 'dl_freq_high': 1495.9,
         'dl_arfcn_low': 4750, 'dl_arfcn_middle': 4850, 'dl_arfcn_high': 4949,
         'dl_bandwidth': 20, 'ul_bandwidth': 20,
         'ul_freq_low': 1427.9, 'ul_freq_middle': 1437.9, 'ul_freq_high': 1447.9,
         'ul_arfcn_low': 22750, 'ul_arfcn_middle': 22850, 'ul_arfcn_high': 22949,
         'duplex_spacing': 48, 'geographical_area': 'Japan',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 12, 'name': '700 a',
         'dl_freq_low': 729, 'dl_freq_middle': 737.5, 'dl_freq_high': 746,
         'dl_arfcn_low': 5010, 'dl_arfcn_middle': 5095, 'dl_arfcn_high': 5179,
         'dl_bandwidth': 17, 'ul_bandwidth': 17,
         'ul_freq_low': 699, 'ul_freq_middle': 707.5, 'ul_freq_high': 716,
         'ul_arfcn_low': 23010, 'ul_arfcn_middle': 23095, 'ul_arfcn_high': 23179,
         'duplex_spacing': 30, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 13, 'name': '700 c',
         'dl_freq_low': 746, 'dl_freq_middle': 751, 'dl_freq_high': 756,
         'dl_arfcn_low': 5180, 'dl_arfcn_middle': 5230, 'dl_arfcn_high': 5279,
         'dl_bandwidth': 10, 'ul_bandwidth': 10,
         'ul_freq_low': 777, 'ul_freq_middle': 782, 'ul_freq_high': 787,
         'ul_arfcn_low': 23180, 'ul_arfcn_middle': 23230, 'ul_arfcn_high': 23279,
         'duplex_spacing': -31, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 14, 'name': '700 PS',
         'dl_freq_low': 758, 'dl_freq_middle': 763, 'dl_freq_high': 768,
         'dl_arfcn_low': 5280, 'dl_arfcn_middle': 5330, 'dl_arfcn_high': 5379,
         'dl_bandwidth': 10, 'ul_bandwidth': 10,
         'ul_freq_low': 788, 'ul_freq_middle': 793, 'ul_freq_high': 798,
         'ul_arfcn_low': 23280, 'ul_arfcn_middle': 23330, 'ul_arfcn_high': 23379,
         'duplex_spacing': -30, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 17, 'name': '700 b',
         'dl_freq_low': 734, 'dl_freq_middle': 740, 'dl_freq_high': 746,
         'dl_arfcn_low': 5730, 'dl_arfcn_middle': 5790, 'dl_arfcn_high': 5849,
         'dl_bandwidth': 12, 'ul_bandwidth': 12,
         'ul_freq_low': 704, 'ul_freq_middle': 710, 'ul_freq_high': 716,
         'ul_arfcn_low': 23730, 'ul_arfcn_middle': 23790, 'ul_arfcn_high': 23849,
         'duplex_spacing': 30, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 18, 'name': '800 Lower',
         'dl_freq_low': 860, 'dl_freq_middle': 867.5, 'dl_freq_high': 875,
         'dl_arfcn_low': 5850, 'dl_arfcn_middle': 5925, 'dl_arfcn_high': 5999,
         'dl_bandwidth': 15, 'ul_bandwidth': 15,
         'ul_freq_low': 815, 'ul_freq_middle': 822.5, 'ul_freq_high': 830,
         'ul_arfcn_low': 23850, 'ul_arfcn_middle': 23925, 'ul_arfcn_high': 23999,
         'duplex_spacing': 45, 'geographical_area': 'Japan',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 19, 'name': '800 Upper',
         'dl_freq_low': 875, 'dl_freq_middle': 882.5, 'dl_freq_high': 890,
         'dl_arfcn_low': 6000, 'dl_arfcn_middle': 6075, 'dl_arfcn_high': 6149,
         'dl_bandwidth': 15, 'ul_bandwidth': 15,
         'ul_freq_low': 830, 'ul_freq_middle': 837.5, 'ul_freq_high': 845,
         'ul_arfcn_low': 24000, 'ul_arfcn_middle': 24075, 'ul_arfcn_high': 24149,
         'duplex_spacing': 45, 'geographical_area': 'Japan',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 20, 'name': '800 DD',
         'dl_freq_low': 791, 'dl_freq_middle': 806, 'dl_freq_high': 821,
         'dl_arfcn_low': 6150, 'dl_arfcn_middle': 6300, 'dl_arfcn_high': 6449,
         'dl_bandwidth': 30, 'ul_bandwidth': 30,
         'ul_freq_low': 832, 'ul_freq_middle': 847, 'ul_freq_high': 862,
         'ul_arfcn_low': 24150, 'ul_arfcn_middle': 24300, 'ul_arfcn_high': 24449,
         'duplex_spacing': -41, 'geographical_area': 'EMEA',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 21, 'name': '1500 Upper',
         'dl_freq_low': 1495.9, 'dl_freq_middle': 1503.4, 'dl_freq_high': 1510.9,
         'dl_arfcn_low': 6450, 'dl_arfcn_middle': 6525, 'dl_arfcn_high': 6599,
         'dl_bandwidth': 15, 'ul_bandwidth': 15,
         'ul_freq_low': 1447.9, 'ul_freq_middle': 1455.4, 'ul_freq_high': 1462.9,
         'ul_arfcn_low': 24450, 'ul_arfcn_middle': 24525, 'ul_arfcn_high': 24599,
         'duplex_spacing': 48, 'geographical_area': 'Japan',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 22, 'name': '3500',
         'dl_freq_low': 3510, 'dl_freq_middle': 3550, 'dl_freq_high': 3590,
         'dl_arfcn_low': 6600, 'dl_arfcn_middle': 7000, 'dl_arfcn_high': 7399,
         'dl_bandwidth': 80, 'ul_bandwidth': 80,
         'ul_freq_low': 3410, 'ul_freq_middle': 3450, 'ul_freq_high': 3490,
         'ul_arfcn_low': 24600, 'ul_arfcn_middle': 25000, 'ul_arfcn_high': 25399,
         'duplex_spacing': 100, 'geographical_area': 'EMEA',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 23, 'name': '2000 S-band',
         'dl_freq_low': 2180, 'dl_freq_middle': 2190, 'dl_freq_high': 2200,
         'dl_arfcn_low': 7500, 'dl_arfcn_middle': 7600, 'dl_arfcn_high': 7699,
         'dl_bandwidth': 20, 'ul_bandwidth': 20,
         'ul_freq_low': 2000, 'ul_freq_middle': 2010, 'ul_freq_high': 2020,
         'ul_arfcn_low': 25500, 'ul_arfcn_middle': 25600, 'ul_arfcn_high': 25699,
         'duplex_spacing': 180, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 24, 'name': '1600 L-band',
         'dl_freq_low': 1525, 'dl_freq_middle': 1542, 'dl_freq_high': 1559,
         'dl_arfcn_low': 7700, 'dl_arfcn_middle': 7870, 'dl_arfcn_high': 8039,
         'dl_bandwidth': 34, 'ul_bandwidth': 34,
         'ul_freq_low': 1626.5, 'ul_freq_middle': 1643.5, 'ul_freq_high': 1660.5,
         'ul_arfcn_low': 25700, 'ul_arfcn_middle': 25870, 'ul_arfcn_high': 26039,
         'duplex_spacing': -101.5, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 25, 'name': '1900+',
         'dl_freq_low': 1930, 'dl_freq_middle': 1962.5, 'dl_freq_high': 1995,
         'dl_arfcn_low': 8040, 'dl_arfcn_middle': 8365, 'dl_arfcn_high': 8689,
         'dl_bandwidth': 65, 'ul_bandwidth': 65,
         'ul_freq_low': 1850, 'ul_freq_middle': 1882.5, 'ul_freq_high': 1915,
         'ul_arfcn_low': 26040, 'ul_arfcn_middle': 26365, 'ul_arfcn_high': 26689,
         'duplex_spacing': 80, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 26, 'name': '850+',
         'dl_freq_low': 859, 'dl_freq_middle': 876.5, 'dl_freq_high': 894,
         'dl_arfcn_low': 8690, 'dl_arfcn_middle': 8865, 'dl_arfcn_high': 9039	,
         'dl_bandwidth': 35, 'ul_bandwidth': 35,
         'ul_freq_low': 814, 'ul_freq_middle': 831.5, 'ul_freq_high': 849,
         'ul_arfcn_low': 26690, 'ul_arfcn_middle': 26865, 'ul_arfcn_high': 27039,
         'duplex_spacing': 45, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 27, 'name': '800 SMR',
         'dl_freq_low': 852, 'dl_freq_middle': 860.5, 'dl_freq_high': 869,
         'dl_arfcn_low': 9040, 'dl_arfcn_middle': 9125, 'dl_arfcn_high': 9209,
         'dl_bandwidth': 17, 'ul_bandwidth': 17,
         'ul_freq_low': 807, 'ul_freq_middle': 815.5, 'ul_freq_high': 824,
         'ul_arfcn_low': 27040, 'ul_arfcn_middle': 27125, 'ul_arfcn_high': 27209,
         'duplex_spacing': 45, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 28, 'name': '700 APT',
         'dl_freq_low': 758, 'dl_freq_middle': 780.5, 'dl_freq_high': 803,
         'dl_arfcn_low': 9210, 'dl_arfcn_middle': 9435, 'dl_arfcn_high': 9659,
         'dl_bandwidth': 45, 'ul_bandwidth': 45,
         'ul_freq_low': 703, 'ul_freq_middle': 725.5, 'ul_freq_high': 748,
         'ul_arfcn_low': 27210, 'ul_arfcn_middle': 27435, 'ul_arfcn_high': 27659,
         'duplex_spacing': 55, 'geographical_area': 'APAC,EU',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 29, 'name': '700 d',
         'dl_freq_low': 717, 'dl_freq_middle': 722.5, 'dl_freq_high': 728,
         'dl_arfcn_low': 9660, 'dl_arfcn_middle': 9715, 'dl_arfcn_high': 9769,
         'dl_bandwidth': 11, 'ul_bandwidth': None,
         'ul_freq_low': None, 'ul_freq_middle': None, 'ul_freq_high': None,
         'ul_arfcn_low': None, 'ul_arfcn_middle': None, 'ul_arfcn_high': None,
         'duplex_spacing': None, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 30, 'name': '2300 WCS',
         'dl_freq_low': 2350, 'dl_freq_middle': 2355, 'dl_freq_high': 2360,
         'dl_arfcn_low': 9770, 'dl_arfcn_middle': 9820, 'dl_arfcn_high': 9869,
         'dl_bandwidth': 10, 'ul_bandwidth': 10,
         'ul_freq_low': 2305, 'ul_freq_middle': 2310, 'ul_freq_high': 2315,
         'ul_arfcn_low': 27660, 'ul_arfcn_middle': 27710, 'ul_arfcn_high': 27759,
         'duplex_spacing': 45, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 31, 'name': '450',
         'dl_freq_low': 462.5, 'dl_freq_middle': 465, 'dl_freq_high': 467.5,
         'dl_arfcn_low': 9870, 'dl_arfcn_middle': 9895, 'dl_arfcn_high': 9919,
         'dl_bandwidth': 5, 'ul_bandwidth': 5,
         'ul_freq_low': 452.5, 'ul_freq_middle': 455, 'ul_freq_high': 457.5,
         'ul_arfcn_low': 27760, 'ul_arfcn_middle': 27785, 'ul_arfcn_high': 27809,
         'duplex_spacing': 10, 'geographical_area': 'Global',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 32, 'name': '1500 L-band',
         'dl_freq_low': 1452, 'dl_freq_middle': 1474, 'dl_freq_high': 1496,
         'dl_arfcn_low': 9920, 'dl_arfcn_middle': 10140, 'dl_arfcn_high': 10359,
         'dl_bandwidth': 44, 'ul_bandwidth': 44,
         'ul_freq_low': None, 'ul_freq_middle': None, 'ul_freq_high': None,
         'ul_arfcn_low': None, 'ul_arfcn_middle': None, 'ul_arfcn_high': None,
         'duplex_spacing': None, 'geographical_area': 'EMEA',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 65, 'name': '2100+',
         'dl_freq_low': 2110, 'dl_freq_middle': 2155, 'dl_freq_high': 2200,
         'dl_arfcn_low': 65536, 'dl_arfcn_middle': 65986, 'dl_arfcn_high': 66435,
         'dl_bandwidth': 90, 'ul_bandwidth': 90,
         'ul_freq_low': 1920, 'ul_freq_middle': 1965, 'ul_freq_high': 2010,
         'ul_arfcn_low': 131072, 'ul_arfcn_middle': 131522, 'ul_arfcn_high': 131971,
         'duplex_spacing': 190, 'geographical_area': 'Global',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 66, 'name': 'AWS-3',
         'dl_freq_low': 2110, 'dl_freq_middle': 2155, 'dl_freq_high': 2200,
         'dl_arfcn_low': 66436, 'dl_arfcn_middle': 66886, 'dl_arfcn_high': 67335,
         'dl_bandwidth': 90, 'ul_bandwidth': 70,
         'ul_freq_low': 1710, 'ul_freq_middle': 1745, 'ul_freq_high': 1780,
         'ul_arfcn_low': 131972, 'ul_arfcn_middle': 132322, 'ul_arfcn_high': 132671,
         'duplex_spacing': 400, 'geographical_area': 'NAR',
         'modified_by': 0, 'added_by': 0},

        {'band_id': 67, 'name': '700 EU',
         'dl_freq_low': 738, 'dl_freq_middle': 748, 'dl_freq_high': 758,
         'dl_arfcn_low': 67336, 'dl_arfcn_middle': 67436, 'dl_arfcn_high': 67535,
         'dl_bandwidth': 20, 'ul_bandwidth': 20,
         'ul_freq_low': None, 'ul_freq_middle': None, 'ul_freq_high': None,
         'ul_arfcn_low': None, 'ul_arfcn_middle': None, 'ul_arfcn_high': None,
         'duplex_spacing': 400, 'geographical_area': 'EMEA',
         'modified_by': 0, 'added_by': 0},
    ])

def downgrade():
    op.drop_table('lte_frequency_bands')
