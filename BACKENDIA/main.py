import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from api.rutas_prediccion import enrutador_prediccion
from base_datos.conexion import SesionLocal
from base_datos.migraciones import inicializar_base_datos

inicializar_base_datos()

aplicacion = FastAPI(
    title="Clasificador General de Imagenes con ImageNet",
    description="API academica para predicciones TOP 5 con MobileNetV2 y ResNet50 preentrenados.",
    version="1.0.0",
)

aplicacion.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origen.strip()
        for origen in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")
        if origen.strip()
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

aplicacion.include_router(enrutador_prediccion)


@aplicacion.get("/")
def inicio():
    return {"mensaje": "Backend de clasificacion de imagenes funcionando"}


@aplicacion.get("/salud")
def salud():
    with SesionLocal() as sesion:
        sesion.execute(text("SELECT 1"))

    return {"estado": "ok", "base_datos": "conectada"}
