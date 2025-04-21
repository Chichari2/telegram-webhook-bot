from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.models import Post
from app.schemas.models import PostSchema


class PostRepository:
  """Repository for handling database operations for Posts."""

  def __init__(self, session: AsyncSession):
    self.session = session

  async def create_post(self, post: PostSchema) -> Post:
    """Create a new post in the database."""
    db_post = Post(**post.dict())
    self.session.add(db_post)
    await self.session.commit()
    await self.session.refresh(db_post)
    return db_post

  async def get_posts(self) -> List[Post]:
    """Retrieve all posts from the database."""
    result = await self.session.execute(select(Post))
    return result.scalars().all()