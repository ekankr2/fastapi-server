# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.domain.post import Post # noqa
from app.domain.post_comment import PostComment # noqa
from app.domain.user import User # noqa