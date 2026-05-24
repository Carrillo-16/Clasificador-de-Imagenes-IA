import time

from sqlalchemy import inspect, text
from sqlalchemy.exc import OperationalError

from base_datos.conexion import motor_base_datos
from base_datos.modelos import Base


def inicializar_base_datos(intentos: int = 10, espera_segundos: float = 2.0):
    ultimo_error = None

    for _ in range(intentos):
        try:
            Base.metadata.create_all(bind=motor_base_datos)
            aplicar_migraciones_simples()
            return
        except OperationalError as error:
            ultimo_error = error
            time.sleep(espera_segundos)

    raise RuntimeError("No fue posible conectar con la base de datos PostgreSQL") from ultimo_error


def aplicar_migraciones_simples():
    inspector = inspect(motor_base_datos)

    if "predicciones" not in inspector.get_table_names():
        return

    columnas = {columna["name"] for columna in inspector.get_columns("predicciones")}
    if "imagen_analizada" in columnas:
        return

    with motor_base_datos.begin() as conexion:
        conexion.execute(
            text("ALTER TABLE predicciones ADD COLUMN imagen_analizada VARCHAR(255) DEFAULT 'imagen_subida' NOT NULL")
        )
