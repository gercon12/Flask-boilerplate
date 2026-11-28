from db import db
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String, DECIMAL, DateTime, ForeignKey, func, Enum as SqlEnum
from datetime import datetime

#Parae crear un Enum
# Debes de hacer la siguiente importacion
from enum import Enum

class SaleStatus(str,Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

#columns: id, code, total, status, created_at, customer_id
class SaleModel(db.Model):
    __tablename__ = 'sales'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(7), unique=True, nullable=False)
    total: Mapped[float] = mapped_column(DECIMAL(10, 4), nullable=False)
    status: Mapped[SaleStatus] = mapped_column(SqlEnum(SaleStatus), default=SaleStatus.PENDING, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    #foreign key
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'), nullable=False)

    #Relacion
    customers = relationship("CustomerModel", back_populates="sales")
    sales_details = relationship("SaleDetailModel", back_populates="sales")