from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class RoleModel(db.Model):
    __tablename__ = 'roles'

    #   nullable=False significa que no puede ser nulo, es decir, debe tener un valor.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)