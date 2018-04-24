"""add user table

Revision ID: 256361a12ea8
Revises: 62238254b5c3
Create Date: 2018-02-03 20:39:42.082000

"""
from alembic import op
import sqlalchemy as sa
import datetime
import datetime
# revision identifiers, used by Alembic.
revision = '256361a12ea8'
down_revision = '62238254b5c3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('pk', sa.Integer, primary_key=True),
        sa.Column('password', sa.String(200), nullable=False),
        sa.Column('username', sa.String(200)),
        sa.Column('is_enabled', sa.Boolean),
        sa.Column('is_account_non_expired', sa.Boolean),
        sa.Column('is_account_non_locked', sa.Boolean),
        sa.Column('is_credentials_non_expired', sa.Boolean),
        sa.Column('token', sa.String(200)),
        sa.Column('first_name', sa.String(200)),
        sa.Column('last_name', sa.String(200)),
        sa.Column('other_names', sa.String(200)),
        sa.Column('job_title', sa.String(200)),
        sa.Column('phone_number', sa.String(200)),
        sa.Column('photo', sa.Text),
        sa.Column('modified_by', sa.Integer),
        sa.Column('added_by', sa.Integer),
        sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow),
        sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
    )
    op.execute('ALTER SEQUENCE  users_pk_seq RENAME TO seq_users_pk')

    users = sa.sql.table(
         'users',
         sa.Column('pk', sa.Integer, sa.Sequence('seq_users_pk', ), primary_key=True, nullable=False),
         sa.Column('password', sa.String(200), nullable=False),
         sa.Column('username', sa.String(200)),
         sa.Column('is_enabled', sa.Boolean),
         sa.Column('is_account_non_expired', sa.Boolean),
         sa.Column('is_account_non_locked', sa.Boolean),
         sa.Column('is_credentials_non_expired', sa.Boolean),
         sa.Column('token', sa.String(200)),
         sa.Column('first_name', sa.String(200)),
         sa.Column('last_name', sa.String(200)),
         sa.Column('other_names', sa.String(200)),
         sa.Column('job_title', sa.String(200)),
         sa.Column('phone_number', sa.String(200)),
         sa.Column('photo', sa.Text),
         sa.Column('modified_by', sa.Integer),
         sa.Column('added_by', sa.Integer),
         sa.Column('date_added', sa.TIMESTAMP, default=datetime.datetime.utcnow,onupdate=datetime.datetime.utcnow),
         sa.Column('date_modified', sa.TIMESTAMP, default=datetime.datetime.utcnow),
    )

    # @TODO: Encrypt password
    op.bulk_insert(users, [
        {
             'username': 'btsuser@bodastage.org',
             'password': 'password',
             'is_enabled': True,
             'token': '123456789123456789',
             'first_name': 'btsuser',
             'last_name': '',
             'job_title': 'Engineer'
         }
    ])

def downgrade():
    op.drop_table('users')
