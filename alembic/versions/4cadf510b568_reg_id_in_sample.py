"""reg id in sample

Revision ID: 4cadf510b568
Revises: 20db9c85577f
Create Date: 2024-03-06 17:17:16.813913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4cadf510b568'
down_revision: Union[str, None] = '20db9c85577f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('samples', sa.Column('registration_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'samples', 'registrations', ['registration_id'], ['id'])
    op.alter_column('testingparameters', 'parameter_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('testingparameters', 'parameter_code',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(None, 'samples', type_='foreignkey')
    op.drop_column('samples', 'registration_id')
    # ### end Alembic commands ###