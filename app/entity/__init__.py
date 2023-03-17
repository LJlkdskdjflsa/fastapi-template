# Import all the models, so that Base has them before being
# imported by Alembic

import database  # noqa
from entity.article_entity import ArticleEntity  # noqa
from entity.feed_entity import FeedEntity  # noqa
from entity.feed_type_entity import FeedTypeEntity  # noqa
from entity.user_entity import UserEntity  # noqa
