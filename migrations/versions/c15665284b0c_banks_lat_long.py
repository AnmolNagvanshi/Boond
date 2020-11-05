"""banks lat-long

Revision ID: c15665284b0c
Revises: 551a3874f914
Create Date: 2020-11-05 12:39:39.885086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c15665284b0c'
down_revision = '551a3874f914'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blood_banks', sa.Column('latitude', sa.Float(), nullable=True))
    op.add_column('blood_banks', sa.Column('longitude', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blood_banks', 'longitude')
    op.drop_column('blood_banks', 'latitude')
    # ### end Alembic commands ###
