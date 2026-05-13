from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Para migrar a SQL Server despues, cambiar esta URL por una cadena compatible
# con SQLAlchemy, por ejemplo: mssql+pyodbc://usuario:clave@servidor/base?driver=ODBC+Driver+17+for+SQL+Server
URL_BASE_DATOS = "sqlite:///./clasificador_imagenes.db"

argumentos_conexion = {"check_same_thread": False} if URL_BASE_DATOS.startswith("sqlite") else {}

motor_base_datos = create_engine(URL_BASE_DATOS, connect_args=argumentos_conexion)
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=motor_base_datos)


def obtener_sesion():
    sesion = SesionLocal()
    try:
        yield sesion
    finally:
        sesion.close()
