from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.db import get_db
from src.models.product import ProductModel, ProductEntity

from src.services.product_service import (delete_product_by_id,
                                          find_all_products,
                                          find_product_by_id, save_product,
                                          update_product)

products_router = APIRouter()

@products_router.get("/")
def root():
    """Raíz de la API."""
    return {"Clean Hub API"}

@products_router.post("/products/", response_model=ProductModel)
def create_new_product(product: ProductModel, db: Session = Depends(get_db)):
    """Crea un nuevo producto."""
    return save_product(db, product)

@products_router.get("/products/", response_model=List[ProductModel])
def list_products(db: Session = Depends(get_db)):
    """Obtiene todos los productos."""
    return find_all_products(db)

@products_router.get("/products/{product_id}", response_model=ProductModel)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Obtiene un producto por su ID."""
    product = find_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@products_router.put("/products/{product_id}", response_model=ProductModel)
def modify_product(product_id: int, updated_data: ProductModel, db: Session = Depends(get_db)):
    """Actualiza un producto existente."""
    product = update_product(db, product_id, updated_data)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product

@products_router.delete("/products/{product_id}")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    """Elimina un producto por su ID."""
    success = delete_product_by_id(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"detail": "Producto eliminado correctamente"}