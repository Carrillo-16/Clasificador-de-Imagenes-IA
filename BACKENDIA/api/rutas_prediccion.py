import os

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from base_datos.conexion import obtener_sesion
from base_datos.operaciones import crear_prediccion, obtener_o_crear_modelo, obtener_o_crear_usuario
from utilidades.archivos import guardar_imagen_analizada
from utilidades.predicciones import predecir_imagen

enrutador_prediccion = APIRouter(tags=["Predicciones"])
TAMANO_MAXIMO_IMAGEN_MB = int(os.getenv("MAX_IMAGE_MB", "8"))
TAMANO_MAXIMO_IMAGEN_BYTES = TAMANO_MAXIMO_IMAGEN_MB * 1024 * 1024


@enrutador_prediccion.post("/predecir")
async def predecir(
    imagen: UploadFile = File(...),
    nombre_modelo: str = Form("MobileNetV2"),
    nombre_usuario: str = Form("Estudiante"),
    correo_usuario: str = Form("estudiante@universidad.com"),
    sesion: Session = Depends(obtener_sesion),
):
    if not imagen.content_type or not imagen.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")

    contenido_imagen = await imagen.read()
    if len(contenido_imagen) > TAMANO_MAXIMO_IMAGEN_BYTES:
        raise HTTPException(status_code=413, detail=f"La imagen no debe superar {TAMANO_MAXIMO_IMAGEN_MB} MB")

    try:
        resultado_prediccion = predecir_imagen(contenido_imagen, nombre_modelo)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    prediccion_principal = resultado_prediccion["predicciones"][0]
    ruta_imagen_analizada = guardar_imagen_analizada(contenido_imagen, imagen.filename)

    usuario = obtener_o_crear_usuario(sesion, nombre_usuario, correo_usuario)
    modelo_ia = obtener_o_crear_modelo(
        sesion,
        resultado_prediccion["modelo"],
        prediccion_principal["porcentaje_confianza"],
    )

    crear_prediccion(
        sesion=sesion,
        imagen_analizada=ruta_imagen_analizada,
        clase_predicha=prediccion_principal["clase"],
        porcentaje_confianza=prediccion_principal["porcentaje_confianza"],
        id_usuario=usuario.id_usuario,
        id_modelo=modelo_ia.id_modelo,
    )

    return {
        "modelo": resultado_prediccion["modelo"],
        "predicciones": [
            {
                "clase": prediccion["clase"],
                "confianza": f"{prediccion['porcentaje_confianza']:.2f}%",
            }
            for prediccion in resultado_prediccion["predicciones"]
        ],
    }
