from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.product import ProductEntity


class ProductRepository:

    def save(db: Session, product: ProductEntity) -> ProductEntity:
        """Creates and saves a product into the database."""
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def find_all(db: Session) -> List[ProductEntity]:
        return db.query(ProductEntity).all()


    def find_by_id(db: Session, product_id: int) -> Optional[ProductEntity]:
        """Find a product by a given id"""
        return db.query(ProductEntity).filter(ProductEntity.id == product_id).first()

    def update(db: Session, product_id: int, updated_data: dict) -> Optional[ProductEntity]:
        """Updates an already existant product."""
        product = db.query(ProductEntity).filter(ProductEntity.id == product_id).first()
        if product:
            for key, value in updated_data.items():
                setattr(product, key, value)
            db.commit()
            db.refresh(product)
        return product


    def delete_by_id(db: Session, product_id: int) -> bool:
        """Deletes a product by its given id."""
        product = db.query(ProductEntity).filter(ProductEntity.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()
            return True
        return False