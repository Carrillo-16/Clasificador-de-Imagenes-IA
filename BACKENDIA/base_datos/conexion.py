import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

URL_BASE_DATOS = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://clasificador_app:ClasificadorIA2026Local@localhost:5432/clasificador_imagenes_ia",
)

argumentos_conexion = {"check_same_thread": False} if URL_BASE_DATOS.startswith("sqlite") else {}

motor_base_datos = create_engine(URL_BASE_DATOS, connect_args=argumentos_conexion, pool_pre_ping=True)
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor_base_datos)


def obtener_sesion():
    sesion = SesionLocal()
    try:
        yield sesion
    finally:
        sesion.close()
