from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False)

    predicciones = relationship("Prediccion", back_populates="usuario")


class ModeloIA(Base):
    __tablename__ = "modelos_ia"

    id_modelo = Column(Integer, primary_key=True, index=True)
    nombre_modelo = Column(String(100), unique=True, nullable=False)
    precision_modelo = Column(Float, default=0.0)

    predicciones = relationship("Prediccion", back_populates="modelo_ia")


class Prediccion(Base):
    __tablename__ = "predicciones"

    id_prediccion = Column(Integer, primary_key=True, index=True)
    imagen_analizada = Column(String(255), nullable=False, default="imagen_subida")
    clase_predicha = Column(String(100), nullable=False)
    porcentaje_confianza = Column(Float, nullable=False)
    fecha_prediccion = Column(DateTime, default=datetime.utcnow)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_modelo = Column(Integer, ForeignKey("modelos_ia.id_modelo"), nullable=False)

    usuario = relationship("Usuario", back_populates="predicciones")
    modelo_ia = relationship("ModeloIA", back_populates="predicciones")
