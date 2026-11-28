#importacion de librerias
from db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean

# columnas: id, name, is_active
class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    #Relacion
    products = relationship("ProductModel", back_populates="categories")

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_active": self.is_active
        }