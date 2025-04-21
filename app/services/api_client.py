import aiohttp
from typing import List, Dict
from app.core.config import settings
from app.schemas.models import PostSchema


class JsonPlaceholderClient:
  """Client for interacting with JSON Placeholder API."""

  def __init__(self):
    self.base_url = settings.API_BASE_URL

  async def get_posts(self) -> List[Dict]:
    """Fetch posts from JSON Placeholder API."""
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{self.base_url}/posts") as response:
        response.raise_for_status()
        return await response.json()

  async def get_post(self, post_id: int) -> Dict:
    """Fetch a single post by ID from JSON Placeholder API."""
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{self.base_url}/posts/{post_id}") as response:
        response.raise_for_status()
        return await response.json()