from sqlalchemy import inspect, text

from base_datos.conexion import motor_base_datos


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
