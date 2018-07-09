"""Create datediff procedure

Revision ID: a04aac3da46d
Revises: 48cc5ed97f92
Create Date: 2018-07-10 02:34:46.762000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a04aac3da46d'
down_revision = '48cc5ed97f92'
branch_labels = None
depends_on = None

class ReplaceableObject(object):
    def __init__(self, name, sqltext):
        self.name = name
        self.sqltext = sqltext

datediff_sp = ReplaceableObject(
    "datediff(type VARCHAR, date_from DATE, date_to DATE)",
    """
    RETURNS INTEGER AS $$
    DECLARE age INTERVAL;
    BEGIN
        age := age(date_to, date_from);
        CASE type
            WHEN 'month' THEN
                RETURN date_part('year', age) * 12 + date_part('month', age);
            WHEN 'year' THEN
                RETURN date_part('year', age);
            ELSE
                RETURN (date_to - date_from)::int;
        END CASE;
    END;
    $$ LANGUAGE plpgsql;
    """
)


def upgrade():
    op.create_sp(datediff_sp)


def downgrade():
    op.drop_sp(datediff_sp)
