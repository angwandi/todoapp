"""empty message

Revision ID: 246f2baaaf75
Revises: c2be97518754
Create Date: 2020-04-07 00:14:04.226739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '246f2baaaf75'
down_revision = 'c2be97518754'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
