"""actually drop pilot table

Revision ID: 9e46b88aa6d7
Revises: f6eefcf0b22f
Create Date: 2026-04-27 23:44:21.978682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e46b88aa6d7'
down_revision: Union[str, Sequence[str], None] = 'f6eefcf0b22f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column('Flight', 'Pilot_ID')

    # op.drop_table('Pilot')
    


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        'Flight',
        sa.Column('Pilot_ID', sa.Integer(), nullable=True)
    )
