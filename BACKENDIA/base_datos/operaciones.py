from sqlalchemy.orm import Session

from base_datos.modelos import ModeloIA, Prediccion, Usuario


def obtener_o_crear_usuario(sesion: Session, nombre: str, correo: str) -> Usuario:
    usuario = sesion.query(Usuario).filter(Usuario.correo == correo).first()
    if usuario:
        return usuario

    usuario = Usuario(nombre=nombre, correo=correo)
    sesion.add(usuario)
    sesion.commit()
    sesion.refresh(usuario)
    return usuario


def obtener_o_crear_modelo(sesion: Session, nombre_modelo: str, precision_modelo: float) -> ModeloIA:
    modelo_ia = sesion.query(ModeloIA).filter(ModeloIA.nombre_modelo == nombre_modelo).first()
    if modelo_ia:
        modelo_ia.precision_modelo = precision_modelo
        sesion.commit()
        sesion.refresh(modelo_ia)
        return modelo_ia

    modelo_ia = ModeloIA(nombre_modelo=nombre_modelo, precision_modelo=precision_modelo)
    sesion.add(modelo_ia)
    sesion.commit()
    sesion.refresh(modelo_ia)
    return modelo_ia


def crear_prediccion(
    sesion: Session,
    imagen_analizada: str,
    clase_predicha: str,
    porcentaje_confianza: float,
    id_usuario: int,
    id_modelo: int,
) -> Prediccion:
    prediccion = Prediccion(
        imagen_analizada=imagen_analizada,
        clase_predicha=clase_predicha,
        porcentaje_confianza=porcentaje_confianza,
        id_usuario=id_usuario,
        id_modelo=id_modelo,
    )
    sesion.add(prediccion)
    sesion.commit()
    sesion.refresh(prediccion)
    return prediccion
