from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Order(Base):
    __tablename__ = "booking"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(150), nullable=False)
    #num : Mapped[int] =  mapped_column(String(11), nullable=False)
    date_from : Mapped[str] = mapped_column(String(150), nullable=False)
    date_to : Mapped[str] = mapped_column(String(150), nullable=False)
    room : Mapped[str] = mapped_column(String(10), nullable=False)
