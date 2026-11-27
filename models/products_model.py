from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text, DECIMAL, Boolean, ForeignKey

#columnas: id, name, code, description, image, brand, size, price, stock, is_active, category_id
class ProductModel(db.Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    image: Mapped[str] = mapped_column(Text, nullable=True)
    brand: Mapped[str] = mapped_column(String(50), nullable=True)
    size: Mapped[str] = mapped_column(String(20), nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(10, 4), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    #llave foranea
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'), nullable=False)