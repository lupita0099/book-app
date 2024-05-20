"""Initial migration.

Revision ID: 942884c59dfa
Revises: 
Create Date: 2024-05-20 16:43:30.528040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '942884c59dfa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('author_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('author_id')
    )
    op.create_table('category',
    sa.Column('category_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('content',
    sa.Column('content_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ISBN', sa.String(length=13), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('type', sa.Enum('book', 'article'), nullable=True),
    sa.Column('publication_year', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('page_length', sa.Integer(), nullable=True),
    sa.Column('cover_image_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('content_id')
    )
    op.create_table('genre',
    sa.Column('genre_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('genre_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('content_author_association',
    sa.Column('content_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.author_id'], ),
    sa.ForeignKeyConstraint(['content_id'], ['content.content_id'], )
    )
    op.create_table('content_category_association',
    sa.Column('content_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.category_id'], ),
    sa.ForeignKeyConstraint(['content_id'], ['content.content_id'], )
    )
    op.create_table('content_genre_association',
    sa.Column('content_id', sa.Integer(), nullable=True),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['content_id'], ['content.content_id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.genre_id'], )
    )
    op.create_table('interactions',
    sa.Column('interaction_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('content_id', sa.Integer(), nullable=True),
    sa.Column('interaction_type', sa.Enum('view', 'like', 'save', 'purchase'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['content_id'], ['content.content_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('interaction_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interactions')
    op.drop_table('content_genre_association')
    op.drop_table('content_category_association')
    op.drop_table('content_author_association')
    op.drop_table('users')
    op.drop_table('genre')
    op.drop_table('content')
    op.drop_table('category')
    op.drop_table('author')
    # ### end Alembic commands ###
