"""empty message

Revision ID: 99a760325eea
Revises: fd723813a60d
Create Date: 2022-08-13 03:22:02.325733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a760325eea'
down_revision = 'fd723813a60d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show', sa.Column('start_time', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('show', 'start_time')
    # ### end Alembic commands ###