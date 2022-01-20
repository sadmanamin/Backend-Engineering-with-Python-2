"""empty message

Revision ID: 2cad17da203a
Revises: 65ef631b243a
Create Date: 2022-01-19 20:46:43.210437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cad17da203a'
down_revision = '65ef631b243a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('body', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'body')
    # ### end Alembic commands ###