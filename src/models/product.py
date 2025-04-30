from typing import Optional

from pydantic import BaseModel, HttpUrl
from sqlalchemy import Boolean, Column, Float, Integer, String, Text

from src.db.db import Base


class ProductModel(BaseModel):
    id: int
    name: str
    price: float
    category: str
    rating: float
    reviews: int
    image: HttpUrl
    is_new: bool
    discount: Optional[int] = 0
    stock: int
    description: str

    class Config:
        form_attributes = True

class ProductEntity(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    reviews = Column(Integer, nullable=False)
    image = Column(Text, nullable=False)
    is_new = Column(Boolean, nullable=False)
    discount = Column(Integer, nullable=True, default=0)  # Opcional con valor por defecto
    stock = Column(Integer, nullable=False)
    description = Column(String, nullable=False)