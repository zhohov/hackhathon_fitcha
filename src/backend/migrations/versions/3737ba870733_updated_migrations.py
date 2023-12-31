"""Updated migrations

Revision ID: 3737ba870733
Revises: 
Create Date: 2023-08-25 12:09:18.798248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3737ba870733'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('folders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('places',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imgURL', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('coord1', sa.String(), nullable=False),
    sa.Column('coord2', sa.String(), nullable=False),
    sa.Column('tag', sa.Integer(), nullable=False),
    sa.Column('city', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('folder_place_association',
    sa.Column('folder_id', sa.Integer(), nullable=True),
    sa.Column('place_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['folder_id'], ['folders.id'], ),
    sa.ForeignKeyConstraint(['place_id'], ['places.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('folder_place_association')
    op.drop_table('places')
    op.drop_table('folders')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_table('cities')
    # ### end Alembic commands ###
