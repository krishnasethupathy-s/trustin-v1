"""add report send  by

Revision ID: bf4117b70318
Revises: 0bc901de9d10
Create Date: 2024-07-13 10:24:09.297462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'bf4117b70318'
down_revision: Union[str, None] = '0bc901de9d10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    sa.Enum('COURIER', 'EMAIL', 'EMAIL_COURIER', 'EMAIL_AND_COURIER', name='reportsentbyenum2').create(op.get_bind())
    op.add_column('registrations', sa.Column('reports_send', postgresql.ENUM('COURIER', 'EMAIL', 'EMAIL_COURIER', 'EMAIL_AND_COURIER', name='reportsentbyenum2', create_type=False), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('registrations', 'reports_send')
    sa.Enum('COURIER', 'EMAIL', 'EMAIL_COURIER', 'EMAIL_AND_COURIER', name='reportsentbyenum2').drop(op.get_bind())
    # ### end Alembic commands ###
