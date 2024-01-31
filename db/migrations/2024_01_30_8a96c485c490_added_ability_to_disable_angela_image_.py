"""added ability to disable Angela image prompts server-wide

Revision ID: 8a96c485c490
Revises: 18140c115341
Create Date: 2024-01-30 22:01:08.868813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a96c485c490'
down_revision: Union[str, None] = '18140c115341'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guild_config', sa.Column('image_deletion_prompts_enabled', sa.Boolean(), nullable=False, default=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guild_config', 'image_deletion_prompts_enabled')
    # ### end Alembic commands ###
