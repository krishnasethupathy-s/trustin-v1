"""add customer_id to batch2

Revision ID: dd08a4b587c4
Revises: f6c041106c56
Create Date: 2024-05-18 09:40:32.412711

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd08a4b587c4'
down_revision: Union[str, None] = 'f6c041106c56'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('batches_customer_id_fkey', 'batches', type_='foreignkey')
    op.create_foreign_key(None, 'batches', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'batches', type_='foreignkey')
    op.create_foreign_key('batches_customer_id_fkey', 'batches', 'products', ['customer_id'], ['id'])
    # ### end Alembic commands ###
