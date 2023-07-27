"""Added about me and last seen fields

Revision ID: 75ebc70fca9f
Revises: 1aee4e004558
Create Date: 2023-07-19 15:58:32.781389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75ebc70fca9f'
down_revision = '1aee4e004558'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###