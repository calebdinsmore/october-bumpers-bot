"""add baby month milestone channel

Revision ID: cf931026a101
Revises: b1deb87ac586
Create Date: 2024-02-02 21:00:50.710390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf931026a101'
down_revision: Union[str, None] = 'b1deb87ac586'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guild_config', sa.Column('baby_month_milestone_channel_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guild_config', 'baby_month_milestone_channel_id')
    # ### end Alembic commands ###
