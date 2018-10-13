"""empty message

Revision ID: 1911cc6c9b15
Revises: b2a97e305de0
Create Date: 2018-10-06 22:33:08.050268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1911cc6c9b15'
down_revision = 'b2a97e305de0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nickname', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nickname')
    # ### end Alembic commands ###