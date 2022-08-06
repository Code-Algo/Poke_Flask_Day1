"""empty message

Revision ID: 70292a1a7d09
Revises: a775fec8d2d4
Create Date: 2022-08-06 14:02:35.806251

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '70292a1a7d09'
down_revision = 'a775fec8d2d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('handler',
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )

    op.add_column('pokemon', sa.Column('name', sa.String(), nullable=True))
    op.add_column('pokemon', sa.Column('ability', sa.String(), nullable=True))
    op.add_column('pokemon', sa.Column('attack', sa.String(), nullable=True))
    op.add_column('pokemon', sa.Column('defence', sa.String(), nullable=True))
    op.add_column('pokemon', sa.Column('hp', sa.String(), nullable=True))
    op.drop_constraint('pokemon_user_id_fkey', 'pokemon', type_='foreignkey')
    op.drop_column('pokemon', 'user_id')
    op.drop_column('pokemon', 'date_updated')
    op.drop_column('pokemon', 'date_created')
    op.drop_column('pokemon', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('pokemon', sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('pokemon', sa.Column('date_updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('pokemon', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pokemon_user_id_fkey', 'pokemon', 'user', ['user_id'], ['id'])
    op.drop_column('pokemon', 'hp')
    op.drop_column('pokemon', 'defence')
    op.drop_column('pokemon', 'attack')
    op.drop_column('pokemon', 'ability')
    op.drop_column('pokemon', 'name')
    op.drop_table('handler')
    # ### end Alembic commands ###