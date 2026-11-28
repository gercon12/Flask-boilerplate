from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, DateTime, func, ForeignKey
from db import db
from datetime import datetime


# ☢️ IMPORTANTE
# Este es un ejemplo de como puedes crear un modelo, se aconseja eliminar este modelo
class UserModel(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    #llave foranea
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'), nullable=False)

    #Establecer las relaciones de las tablas
    #Para poder acceder a los datos de una forma mas sencilla
    #users N:1 roles

    role = relationship("RoleModel", back_populates = "users")








