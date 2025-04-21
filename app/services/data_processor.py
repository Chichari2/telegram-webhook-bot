from typing import List, Dict
import re
from pydantic import ValidationError
from app.schemas.models import PostSchema


class DataProcessor:
  """Service for processing data from API."""

  @staticmethod
  def camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

  def convert_keys_to_snake_case(self, data: Dict) -> Dict:
    """Convert all dictionary keys from camelCase to snake_case."""
    return {self.camel_to_snake(key): value for key, value in data.items()}

  async def process_posts(self, raw_posts: List[Dict]) -> List[PostSchema]:
    """Process raw posts data from API."""
    processed_posts = []
    for post in raw_posts:
      try:
        snake_case_post = self.convert_keys_to_snake_case(post)
        validated_post = PostSchema(**snake_case_post)
        processed_posts.append(validated_post)
      except ValidationError as e:
        print(f"Validation error for post {post.get('id')}: {e}")
        continue
    return processed_posts