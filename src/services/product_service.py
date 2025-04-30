from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.product import ProductModel, ProductEntity
from src.repositories.product_repository.product_repository import ProductRepository


def save_product(db: Session, product_data: ProductModel) -> ProductEntity:
    """Convierte ProductModel a ProductEntity y lo guarda en la base de datos."""
    new_product = ProductEntity(**product_data.dict())
    new_product.image = str(new_product.image)
    saved_product = ProductRepository.save(db, new_product)
    return saved_product


def find_all_products(db: Session) -> List[ProductEntity]:
    """Obtiene todos los productos y los convierte a ProductModel."""
    return ProductRepository.find_all(db)


def find_product_by_id(db: Session, product_id: int) -> Optional[ProductEntity]:
    """Obtiene un producto por su ID y lo convierte a ProductModel."""
    product = ProductRepository.find_by_id(db, product_id)
    if product:
        return product
    return None


def update_product(db: Session, product_id: int, updated_data: ProductModel) -> Optional[ProductEntity]:
    """Convierte ProductModel a un diccionario y actualiza el producto."""
    updated_data.image = str(updated_data.image)
    updated_entity = ProductRepository.update(db, product_id, updated_data.dict(exclude_unset=True))
    
    if updated_entity:
        return updated_entity
    return None


def delete_product_by_id(db: Session, product_id: int) -> bool:
    """Elimina un producto por su ID."""
    return ProductRepository.delete_by_id(db, product_id)