from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float, ForeignKey


#columns: id, quantity, price, total, product_id,sale_id
class SaleDetailModel(db.Model):
    __tablename__ = 'sales_details'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    total: Mapped[float] = mapped_column(Float, nullable=False)

    #foreign keys
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'), nullable=False)
    sale_id: Mapped[int] = mapped_column(Integer, ForeignKey('sales.id'), nullable=False)