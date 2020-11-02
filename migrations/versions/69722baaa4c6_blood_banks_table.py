"""blood_banks table

Revision ID: 69722baaa4c6
Revises: 5291db81d094
Create Date: 2020-11-02 15:07:28.136379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69722baaa4c6'
down_revision = '5291db81d094'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blood_banks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('mobile_no', sa.String(length=10), nullable=False),
    sa.Column('address', sa.String(length=400), nullable=False),
    sa.Column('state', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('pin_code', sa.String(length=6), nullable=False),
    sa.Column('latitude', sa.String(length=20), nullable=True),
    sa.Column('longitude', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blood_banks_email'), 'blood_banks', ['email'], unique=True)
    op.create_index(op.f('ix_blood_banks_name'), 'blood_banks', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blood_banks_name'), table_name='blood_banks')
    op.drop_index(op.f('ix_blood_banks_email'), table_name='blood_banks')
    op.drop_table('blood_banks')
    # ### end Alembic commands ###
