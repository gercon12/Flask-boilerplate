from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

#columnas: id, name, is_active
class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)