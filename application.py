from os import getenv

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from src.models.product import ProductEntity
from src.routers.products import products_router




app = FastAPI(
    title="CLEAN-HU-API",
    description="Proyecto clean hub desarrollado para entregable Politécnico GranColombiano.", 
    version="1.0",
    contact={
        "name":"Clean hub proyect",
        "url":"dpaarizal@poligran.edu.co"
    }    
)

router = APIRouter()

origins=[
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:3000/",
    getenv("FRONTEND_URL")
]

# CORS Middleware config

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# API Routers setup
app.include_router(router)  
app.include_router(products_router)

# Create the tables in the database with specified order.
tables=[ProductEntity.__table__]