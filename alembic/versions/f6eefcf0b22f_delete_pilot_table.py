"""delete pilot table

Revision ID: f6eefcf0b22f
Revises: 5d465d473df4
Create Date: 2026-04-27 23:12:27.638528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6eefcf0b22f'
down_revision: Union[str, Sequence[str], None] = '5d465d473df4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_table('pilot')
    


def downgrade() -> None:
    """Downgrade schema."""
    op.create_table(
        'pilot',
        sa.Column('id', sa.Integer, primary_key=True),
    )
