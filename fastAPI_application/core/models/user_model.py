from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base_model import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    login: Mapped[str] = mapped_column(String(50), nullable=False)
    hash_password: Mapped[str] = mapped_column(String(255),nullable=False)