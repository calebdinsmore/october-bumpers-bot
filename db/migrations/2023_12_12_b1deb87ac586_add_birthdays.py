"""add birthdays

Revision ID: b1deb87ac586
Revises: 84abfe2ccee0
Create Date: 2023-12-12 21:15:21.827946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1deb87ac586'
down_revision: Union[str, None] = '84abfe2ccee0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birthdays',
    sa.Column('guild_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('guild_id', 'user_id', 'name')
    )
    op.create_index(op.f('ix_birthdays_guild_id_user_id'), 'birthdays', ['guild_id', 'user_id'], unique=False)
    op.create_table('guild_config',
    sa.Column('guild_id', sa.Integer(), nullable=False),
    sa.Column('birthday_channel_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('guild_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guild_config')
    op.drop_index(op.f('ix_birthdays_guild_id_user_id'), table_name='birthdays')
    op.drop_table('birthdays')
    # ### end Alembic commands ###
