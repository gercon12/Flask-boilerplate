from pydantic import BaseModel, Field

#Validar datos de la categoria
class CategorySchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    