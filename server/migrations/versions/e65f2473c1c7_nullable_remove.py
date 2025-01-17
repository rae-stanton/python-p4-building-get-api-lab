"""nullable remove

Revision ID: e65f2473c1c7
Revises: 4932e577198c
Create Date: 2023-10-04 15:44:05.907125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e65f2473c1c7'
down_revision = '4932e577198c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.alter_column('bakery_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.alter_column('bakery_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
