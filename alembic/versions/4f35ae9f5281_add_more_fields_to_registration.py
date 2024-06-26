"""add more fields to registration

Revision ID: 4f35ae9f5281
Revises: 84aa9e6a3964
Create Date: 2024-05-30 21:20:16.906087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4f35ae9f5281'
down_revision: Union[str, None] = '84aa9e6a3964'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('registrations', sa.Column('test_type_id', sa.Integer(), nullable=False))
    op.add_column('registrations', sa.Column('product_id', sa.Integer(), nullable=False))
    op.add_column('registrations', sa.Column('testing_process', postgresql.ENUM('BATCH_ANALYSIS', 'METHOD_DEVELOPMENT', 'METHOD_VALIDATION', 'RD_RESEARCH', 'REGULATORY', name='testingprocessenum', create_type=False), nullable=False))
    op.add_column('registrations', sa.Column('license_no', sa.String(), nullable=True))
    op.add_column('registrations', sa.Column('sampled_by', postgresql.ENUM('CUSTOMER', 'LABORATORY', name='samplingbyenum', create_type=False), nullable=True))
    op.add_column('registrations', sa.Column('sample_disposal_process', postgresql.ENUM('DISCARD', 'RETURN', name='disposalprocessenum', create_type=False), nullable=True))
    op.add_column('registrations', sa.Column('reports_send_by', postgresql.ENUM('COURIER', 'EMAIL', name='reportsentbyenum', create_type=False), nullable=True))
    op.alter_column('registrations', 'nabl_logo',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('registrations', 'no_of_samples',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('registrations_product_fkey', 'registrations', type_='foreignkey')
    op.create_foreign_key(None, 'registrations', 'testtypes', ['test_type_id'], ['id'])
    op.create_foreign_key(None, 'registrations', 'products', ['product_id'], ['id'])
    op.drop_column('registrations', 'product')
    op.drop_constraint('samples_batch_id_fkey', 'samples', type_='foreignkey')
    op.drop_column('samples', 'name')
    op.drop_column('samples', 'batch_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('samples', sa.Column('batch_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('samples', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key('samples_batch_id_fkey', 'samples', 'batches', ['batch_id'], ['id'])
    op.add_column('registrations', sa.Column('product', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'registrations', type_='foreignkey')
    op.drop_constraint(None, 'registrations', type_='foreignkey')
    op.create_foreign_key('registrations_product_fkey', 'registrations', 'products', ['product'], ['id'])
    op.alter_column('registrations', 'no_of_samples',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('registrations', 'nabl_logo',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_column('registrations', 'reports_send_by')
    op.drop_column('registrations', 'sample_disposal_process')
    op.drop_column('registrations', 'sampled_by')
    op.drop_column('registrations', 'license_no')
    op.drop_column('registrations', 'testing_process')
    op.drop_column('registrations', 'product_id')
    op.drop_column('registrations', 'test_type_id')
    # ### end Alembic commands ###
