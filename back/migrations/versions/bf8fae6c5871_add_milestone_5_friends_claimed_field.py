"""Add milestone_5_friends_claimed field

Revision ID: bf8fae6c5871
Revises: 2062d72a632b
Create Date: 2025-06-14 04:37:26.143341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bf8fae6c5871'
down_revision: Union[str, None] = '2062d72a632b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('milestone_5_friends_claimed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'milestone_5_friends_claimed')
    # ### end Alembic commands ###
