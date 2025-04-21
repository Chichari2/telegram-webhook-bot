from pydantic import BaseModel


class PostSchema(BaseModel):
  """Pydantic model for Post data validation."""
  user_id: int
  id: int
  title: str
  body: str

  class Config:
    alias_generator = lambda x: x  # Disable alias generation
    allow_population_by_field_name = True