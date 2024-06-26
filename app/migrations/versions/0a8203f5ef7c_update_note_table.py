"""update note table

Revision ID: 0a8203f5ef7c
Revises: 5cefef33a263
Create Date: 2024-03-31 23:31:36.654152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a8203f5ef7c'
down_revision = '5cefef33a263'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###
