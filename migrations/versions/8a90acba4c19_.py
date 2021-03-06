"""empty message

Revision ID: 8a90acba4c19
Revises: 
Create Date: 2019-10-05 11:38:29.339966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a90acba4c19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_config_description'), 'config', ['description'], unique=False)
    op.create_index(op.f('ix_config_key'), 'config', ['key'], unique=True)
    op.create_index(op.f('ix_config_value'), 'config', ['value'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_config_value'), table_name='config')
    op.drop_index(op.f('ix_config_key'), table_name='config')
    op.drop_index(op.f('ix_config_description'), table_name='config')
    op.drop_table('config')
    # ### end Alembic commands ###
