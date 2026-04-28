"""drop unused tables

Revision ID: c3045c8d4e80
Revises: 8c81a2f83e0f
Create Date: 2026-04-27 21:47:13.940299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3045c8d4e80'
down_revision: Union[str, Sequence[str], None] = '8c81a2f83e0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint('FK__Pilot__Airline_I__48CFD27E', 'pilot', type_='foreignkey')


def downgrade() -> None:
    """Downgrade schema."""
    pass
