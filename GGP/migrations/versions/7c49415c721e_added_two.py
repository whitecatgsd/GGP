"""added two

Revision ID: 7c49415c721e
Revises: 
Create Date: 2017-04-27 17:30:35.355115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c49415c721e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('clickimg1', sa.String(length=80), nullable=True))
    op.add_column('users', sa.Column('clickimg2', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'clickimg2')
    op.drop_column('users', 'clickimg1')
    # ### end Alembic commands ###