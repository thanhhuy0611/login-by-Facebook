"""empty message

Revision ID: 8271daac6bc4
Revises: c35d8dd4924a
Create Date: 2019-11-27 16:35:47.512774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8271daac6bc4'
down_revision = 'c35d8dd4924a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    # ### end Alembic commands ###
