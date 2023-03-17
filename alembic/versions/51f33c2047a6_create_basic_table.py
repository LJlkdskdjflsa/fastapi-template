"""create basic table

Revision ID: 51f33c2047a6
Revises:
Create Date: 2023-03-09 22:53:41.891112

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '51f33c2047a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 新增 User 表格
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_name', sa.String(length=255), nullable=False),
        sa.Column('photo_url', sa.String(length=255), nullable=True),
        sa.Column('user_address', sa.String(length=255), nullable=False),
        sa.Column('share', sa.JSON(), nullable=True),
        sa.Column('nft', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )

    # 新增 Feed 表格
    op.create_table(
        'feed',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('type_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['type_id'], ['feed_type.id']),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id'),
    )

    # 新增 FeedType 表格
    op.create_table(
        'feed_type',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('meta', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )

    # 新增 Article 表格
    op.create_table(
        'article',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('author_id', sa.Integer(), nullable=False),
        sa.Column('feed_id', sa.Integer(), nullable=False),
        sa.Column('created_time', sa.DateTime(), nullable=False),
        sa.Column('source_url', sa.String(length=255), nullable=False),
        sa.ForeignKeyConstraint(['author_id'], ['user.id']),
        sa.ForeignKeyConstraint(['feed_id'], ['feed.id']),
        sa.PrimaryKeyConstraint('id'),
    )

    # 新增 subscripted_feed_id 欄位至 User 表格
    op.add_column('user', sa.Column('subscripted_feed_id', sa.ARRAY(sa.Integer()), nullable=True))
    op.create_index(op.f('ix_user_subscripted_feed_id'), 'user', ['subscripted_feed_id'], unique=False)


def downgrade() -> None:
    # 刪除 subscripted_feed_id 欄位及相關 index
    op.drop_index(op.f('ix_user_subscripted_feed_id'), table_name='user')
    op.drop_column('user', 'subscripted_feed_id')

    # 刪除 Article 表格
    op.drop_table('article')

    # 刪除 FeedType 表格
    op.drop_table('feed_type')

    # 刪除 Feed 表格
    op.drop_table('feed')

    # 刪除 User 表格
    op.drop_table('user')
